---
description: Provision a fresh homelab server from scratch using Ansible
---

# Fresh Server Setup

## Prerequisites
- A fresh Ubuntu/Debian server accessible via SSH
- Update `ansible/inventory.ini` with the server's IP address
- Ansible installed locally (`pip install ansible`)

## Steps

1. Update the server IP in `ansible/inventory.ini`:
```ini
[homelab_servers]
server1 ansible_host=NEW_IP ansible_user=floki ansible_ssh_common_args='-o StrictHostKeyChecking=no'
```

2. Update all config files that reference the server IP:
   - `docker/homepage_config/services.yaml` — all `href` URLs
   - `docker/docker-compose.yml` — BookStack `APP_URL`

3. Run the server setup playbook (installs Docker, creates directories):
```powershell
cd ansible
ansible-playbook -i inventory.ini server_setup.yml --ask-pass --ask-become-pass
```

4. Upgrade Docker Compose to v2 (the Ansible playbook installs v1 by default):
```powershell
ssh floki@SERVER_IP "sudo curl -L 'https://github.com/docker/compose/releases/download/v2.24.5/docker-compose-linux-x86_64' -o /usr/local/bin/docker-compose && sudo chmod +x /usr/local/bin/docker-compose"
```

5. Deploy all services:
```powershell
ansible-playbook -i inventory.ini deploy_core_services.yml --ask-pass --ask-become-pass
```

6. Verify deployment using the `/check-status` workflow.

## Post-Setup
- Change default passwords for: BookStack (`admin@admin.com` / `password`), NPM (`admin@example.com` / `changeme`)
- Configure AdGuard Home initial setup at `http://SERVER_IP:3000`
- Claim Plex server at `http://SERVER_IP:32400/web`
