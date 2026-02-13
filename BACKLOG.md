# Homelab Backlog

Things I want to set up, organized by category. Move items to **Done** when completed.

---

## 🔴 High Priority

- [ ] **HTTPS for Vaultwarden** — Configure NPM reverse proxy with SSL so Vaultwarden works properly in the browser
- [ ] **Automated Backups** — Set up a cron job or script to back up critical container data (Vaultwarden, Home Assistant, BookStack)
- [ ] **Move secrets to `.env`** — Move BookStack `APP_KEY`, database passwords, and other secrets out of `docker-compose.yml` into `.env`

## 🟡 Medium Priority

### Networking & Security
- [ ] **Tailscale VPN** — Enable remote access to homelab without port forwarding (role exists in Ansible but not deployed)
- [ ] **Pi-hole or AdGuard DNS setup** — Finish configuring AdGuard Home as the network DNS server
- [ ] **Fail2Ban** — Add brute-force protection to SSH and exposed services

### Media & Downloads
- [ ] **Jellyfin** — Open-source alternative/complement to Plex
- [ ] **Sonarr** — Automated TV show management
- [ ] **Radarr** — Automated movie management
- [ ] **Prowlarr** — Indexer manager for Sonarr/Radarr
- [ ] **Transmission/qBittorrent** — Download client

### Productivity & Tools
- [ ] **Nextcloud** — Self-hosted cloud storage and collaboration
- [ ] **Gitea** — Self-hosted Git server
- [ ] **Paperless-ngx** — Document management and OCR scanning
- [ ] **Mealie** — Recipe manager

### Monitoring
- [ ] **Grafana + Prometheus** — Advanced monitoring dashboards for server metrics
- [ ] **cAdvisor** — Container-level resource monitoring

## 🟢 Nice to Have

- [ ] **Immich** — Self-hosted Google Photos alternative
- [ ] **Audiobookshelf** — Audiobook and podcast server
- [ ] **Calibre-Web** — eBook library
- [ ] **Heimdall** — Alternative dashboard (or keep Homepage)
- [ ] **Watchtower** — Auto-update Docker containers
- [ ] **Traefik** — Alternative reverse proxy with auto-SSL (replace NPM)

---

## ✅ Done

- [x] **BookStack** — Wiki & documentation (port 6875)
- [x] **Homepage Dashboard** — Service dashboard (port 7575)
- [x] **Portainer** — Docker management (port 9000)
- [x] **Vaultwarden** — Password manager (port 8080)
- [x] **Plex** — Media server (port 32400)
- [x] **Uptime Kuma** — Status monitoring (port 3001)
- [x] **Syncthing** — File sync (port 8384)
- [x] **Home Assistant** — Home automation (port 8123)
- [x] **AdGuard Home** — DNS & ad blocking (port 80)
- [x] **Nginx Proxy Manager** — Reverse proxy (port 81)
