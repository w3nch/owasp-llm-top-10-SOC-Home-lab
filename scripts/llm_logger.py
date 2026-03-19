import datetime
import json
import os
import sys

import requests
from flask import Flask, Response, request

app = Flask(__name__)

OLLAMA_BASE = "http://localhost:11434"
LOG_DIR = "/var/ossec/logs"
LOG_FILE = f"{LOG_DIR}/llm.log"


def require_root():
    if os.geteuid() != 0:
        print("[ERROR] Run this script as root")
        sys.exit(1)


def setup_logging():
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(LOG_FILE):
        open(LOG_FILE, "a").close()
    try:
        os.chmod(LOG_DIR, 0o777)
        os.chmod(LOG_FILE, 0o666)
    except:
        pass


def log_event(data):
    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(data) + "\n")
    except:
        pass


def clean_headers(headers):
    excluded = [
        "host",
        "content-length",
        "transfer-encoding",
        "connection",
        "accept-encoding",
    ]
    return {k: v for k, v in headers if k.lower() not in excluded}


@app.route("/", methods=["GET"])
def health():
    return {"status": "ok"}


@app.route("/api/<path:path>", methods=["GET", "POST", "PUT", "DELETE"])
def proxy(path):
    url = f"{OLLAMA_BASE}/api/{path}"

    headers = clean_headers(request.headers)

    try:
        request_json = request.get_json()
    except:
        request_json = None

    try:
        if request_json is not None:
            resp = requests.request(
                method=request.method,
                url=url,
                headers=headers,
                json=request_json,
                cookies=request.cookies,
                allow_redirects=False,
            )
        else:
            resp = requests.request(
                method=request.method,
                url=url,
                headers=headers,
                data=request.get_data(),
                cookies=request.cookies,
                allow_redirects=False,
            )
    except Exception as e:
        return Response(f"Proxy error: {e}", status=500)

    response_text = ""
    try:
        response_json = resp.json()

        if isinstance(response_json, dict):
            if "response" in response_json:
                response_text = response_json["response"]

            if "message" in response_json and "content" in response_json["message"]:
                response_text = response_json["message"]["content"]

    except:
        response_text = resp.text

    log = {
        "timestamp": str(datetime.datetime.now()),
        "endpoint": f"/api/{path}",
        "method": request.method,
        "request": request_json,
        "response": response_text,
    }

    log_event(log)

    return Response(
        resp.content,
        status=resp.status_code,
        content_type=resp.headers.get("Content-Type", "application/json"),
    )


if __name__ == "__main__":
    require_root()
    setup_logging()
    app.run(host="0.0.0.0", port=5000)
