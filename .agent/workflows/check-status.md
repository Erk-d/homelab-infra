---
description: Check health and status of all homelab containers
---

# Check Homelab Status

// turbo-all

## Steps

1. Check all container statuses:
```powershell
ssh floki@192.168.68.75 "docker ps -a --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'"
```

2. Check disk usage on the server:
```powershell
ssh floki@192.168.68.75 "df -h / && echo '---' && du -sh ~/app/*/ 2>/dev/null | sort -rh | head -10"
```

3. Check for containers that are restarting or exited:
```powershell
ssh floki@192.168.68.75 "docker ps -a --filter 'status=exited' --filter 'status=restarting' --format '{{.Names}}: {{.Status}}'"
```

4. If any containers are unhealthy, check their logs:
```powershell
ssh floki@192.168.68.75 "docker logs --tail 20 CONTAINER_NAME"
```

## Service Port Reference

| Service | Port | URL |
|---|---|---|
| NPM Admin | 81 | `http://192.168.68.75:81` |
| AdGuard Home | 80 (host) | `http://192.168.68.75` |
| Home Assistant | 8123 (host) | `http://192.168.68.75:8123` |
| Portainer | 9000 | `http://192.168.68.75:9000` |
| Uptime Kuma | 3001 | `http://192.168.68.75:3001` |
| Vaultwarden | 8080 | `http://192.168.68.75:8080` |
| Plex | 32400 (host) | `http://192.168.68.75:32400/web` |
| Homepage | 7575 | `http://192.168.68.75:7575` |
| Syncthing | 8384 | `http://192.168.68.75:8384` |
| BookStack | 6875 | `http://192.168.68.75:6875` |
