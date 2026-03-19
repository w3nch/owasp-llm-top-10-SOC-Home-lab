# Wazuh Deployment (Docker - Single Node)

This section describes how to deploy **Wazuh** using Docker in a **single-node configuration** for the LLM Security SOC Home Lab.

Wazuh provides:

• Log collection and analysis  
• Threat detection and alerting  
• SIEM capabilities for security monitoring  

Official documentation:
```url
https://documentation.wazuh.com/current/deployment-options/docker/wazuh-container.html
```

## Overview

The Wazuh Docker deployment includes the following components:

• **Wazuh Manager** – Processes logs and applies detection rules  
• **Wazuh Indexer** – Stores and indexes log data  
• **Wazuh Dashboard** – Web interface for monitoring and analysis  

The single-node setup is suitable for:

• Local lab environments  
• Testing and development  
• Security research setups  


## Clone Wazuh Docker Repository

Download the official Wazuh Docker configuration:

```bash
git clone https://github.com/wazuh/wazuh-docker.git
cd wazuh-docker/single-node
```

This repository contains pre-configured Docker Compose files for deploying Wazuh.


## Generate Certificates

Before starting the stack, generate the required SSL certificates:

```bash
docker compose -f generate-indexer-certs.yml run --rm generator
```

### What This Step Does

• Generates TLS certificates for secure communication  
• Prepares the indexer and dashboard for encrypted connections  
• Ensures proper authentication between components  


## Start Wazuh Stack

Run the full Wazuh environment:

```bash
docker compose up -d
```

### What This Command Does

• Starts all Wazuh services in detached mode  
• Deploys manager, indexer, and dashboard containers  
• Initializes the SIEM environment  


## Verify Deployment

Check running containers:

```bash
docker ps
```

You should see containers similar to:

• wazuh-manager  
• wazuh-indexer  
• wazuh-dashboard  


## Access Wazuh Dashboard

Once the containers are running, access the web interface:

```url
https://<your-server-ip>
```

Default credentials:

```text
Username: admin  
Password: SecretPassword
```

> Note: You may be prompted to accept a self-signed certificate.


## Initial Setup Notes

• The dashboard may take a few minutes to become fully available  
• Indexing services need time to initialize  
• Logs may not appear immediately after startup  


## Integration with Logging Pipeline

To integrate with the LLM logging pipeline:

• Ensure logs are written to:  
```bash
/var/ossec/logs/llm.log
```

• Configure Wazuh agent (if required) to monitor this file  
• Verify logs are being ingested in the dashboard  


## Troubleshooting

### Containers Not Starting

```bash
docker compose logs -f
```

Check logs for errors related to:

• Port conflicts  
• Missing certificates  
• Resource constraints  


### Dashboard Not Accessible

• Verify ports are open  
• Check container status  
• Ensure HTTPS is used  

### No Logs in Dashboard

• Confirm log file exists  
• Verify correct file path  
• Check Wazuh manager logs  


## Next Steps

- [x] Install and configure **Ollama**  
- [x] Deploy **Open WebUI**  
- [x] Configure the **LLM logging pipeline**  
- [x] Deploy **Wazuh SIEM**  
- [ ] Create **LLM attack simulations**  
- [ ] Implement **SOC detection rules for LLM threats**  


## Notes

This deployment enables:

• Centralized log monitoring  
• Real-time threat detection  
• Visualization of LLM activity  
• SOC-style security analysis within the lab
