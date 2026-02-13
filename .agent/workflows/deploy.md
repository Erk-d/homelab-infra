---
description: Deploy homelab changes to server (docker-compose + homepage config)
---

# Deploy Homelab

// turbo-all

## Prerequisites
- Server: `192.168.68.75`, User: `floki`
- Working directory on server: `~/app`
- Docker Compose v2 installed at `/usr/local/bin/docker-compose`

## Steps

1. Verify server is reachable:
```powershell
Test-Connection -ComputerName 192.168.68.75 -Count 1
```

2. Copy `docker-compose.yml` to server:
```powershell
scp docker/docker-compose.yml floki@192.168.68.75:app/docker-compose.yml
```

3. Copy `.env` file to server (if it exists locally):
```powershell
scp docker/.env floki@192.168.68.75:app/.env
```

4. Copy Homepage config to server:
```powershell
scp docker/homepage_config/services.yaml floki@192.168.68.75:app/homepage_config/services.yaml
```

5. SSH in and bring up services:
```powershell
ssh floki@192.168.68.75 "cd ~/app && docker-compose up -d --remove-orphans"
```

6. Verify all containers are running:
```powershell
ssh floki@192.168.68.75 "docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"
```

7. Confirm Homepage is accessible at `http://192.168.68.75:7575`
