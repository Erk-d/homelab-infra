---
description: Backup homelab Docker volumes and configs
---

# Backup Homelab Data

## Steps

1. SSH into the server:
```powershell
ssh floki@192.168.68.75
```

2. Stop all containers (to ensure data consistency):
```bash
cd ~/app && docker-compose stop
```

3. Create a timestamped backup of all service data:
```bash
BACKUP_DIR=~/backups/$(date +%Y-%m-%d)
mkdir -p $BACKUP_DIR
cd ~/app

# Backup each service's data directory
for dir in npm portainer_data uptime_kuma_data vaultwarden_data homeassistant_config adguard_conf adguard_work syncthing_config plex homepage_config bookstack; do
  if [ -d "$dir" ]; then
    echo "Backing up $dir..."
    tar czf "$BACKUP_DIR/$dir.tar.gz" "$dir"
  fi
done

echo "Backup complete: $BACKUP_DIR"
ls -lh $BACKUP_DIR
```

4. Restart all containers:
```bash
docker-compose up -d
```

5. (Optional) Copy backup to your local machine:
```powershell
scp -r floki@192.168.68.75:~/backups/YYYY-MM-DD ./backups/
```

## Critical Data to Protect
| Service | Data Dir | Priority |
|---|---|---|
| Vaultwarden | `vaultwarden_data/` | 🔴 Critical (passwords) |
| Home Assistant | `homeassistant_config/` | 🟠 High (automations) |
| BookStack | `bookstack/` | 🟡 Medium (wiki content) |
| AdGuard | `adguard_conf/` | 🟡 Medium (DNS rules) |
| NPM | `npm/` | 🟡 Medium (proxy configs) |
| Uptime Kuma | `uptime_kuma_data/` | 🟢 Low (monitors) |
