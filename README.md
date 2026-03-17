# SOC Home Lab – OWASP Top 10 for LLM Applications

This repository documents my **AI Security / SOC home lab** designed to study and detect vulnerabilities from the **OWASP Top 10 for Large Language Model Applications**.

The goal of this lab is to simulate attacks against LLM-powered applications and practice **security monitoring, detection engineering, and incident response**.

---

## Lab Goals

* Understand security risks in LLM applications
* Simulate real AI attacks
* Build detection rules for LLM threats
* Practice SOC investigation workflows
* Study OWASP Top 10 for LLM

---

## Technologies Used

LLM Infrastructure

* Ollama
* Llama3 / Mistral

Vulnerable AI Applications

* Prompt Injection Lab
* OWASP GenAI Security Projects

SOC Stack

* Wazuh
* Elasticsearch
* Kibana

Offensive Testing

* Kali Linux
* Custom attack scripts

---

## Lab Architecture

See:

architecture/lab_architecture.md

---

## Lab Setup

Step-by-step setup documentation:

* infrastructure setup
* local LLM installation
* vulnerable AI applications
* SOC monitoring stack

Documentation available inside the **setup** folder.

---

## Simulated Attacks

The lab includes demonstrations of attacks from the OWASP Top 10 for LLM applications:

* Prompt Injection
* Data Exfiltration
* Jailbreak Attacks
* Tool Injection
* RAG Poisoning

See the **attacks** directory.

---

## Detection Engineering

The lab includes:

* Wazuh detection rules
* Sigma rules
* alert monitoring

See the **detection-rules** folder.

---

## Example Incident Investigation

Example SOC investigation workflow is documented in:

investigations/incident-analysis.md

---

## Screenshots

Screenshots of attacks and SOC alerts are stored in the **screenshots** folder.

---

## Learning Objectives

This lab helps practice:

* AI security
* LLM red teaming
* SOC monitoring
* detection engineering
* incident response

---

## Disclaimer

This lab is built **for educational and research purposes only**.
