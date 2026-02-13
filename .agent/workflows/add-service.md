---
description: Add a new Docker service to the homelab stack
---

# Add a New Service

## Steps

1. **Edit `docker/docker-compose.yml`** — Add the new service definition:
   - Use `container_name` matching the service name
   - Set `restart: unless-stopped`
   - Map volumes to `./service_name_data:/path` (relative to compose dir)
   - Add environment variables (use `${VAR}` for secrets stored in `.env`)
   - Expose ports with explicit host:container mapping

2. **Update `.gitignore`** — Add the service's data directory so live data isn't committed:
   ```
   service_name_data/
   ```

3. **Update Homepage dashboard** — Edit `docker/homepage_config/services.yaml`:
   - Add the service under the appropriate category (Infrastructure, Media & Files, Monitoring & Tools, Documentation)
   - Use the format:
     ```yaml
     - ServiceName:
         icon: service-name.png
         href: "http://192.168.68.75:PORT"
         description: Short description
     ```

4. **Deploy** — Run the `/deploy` workflow to push changes to the server.

5. **Verify** — Confirm the new service is running:
   ```powershell
   ssh floki@192.168.68.75 "docker ps | grep service_name"
   ```

6. **Commit** — Push changes to GitHub:
   ```powershell
   git add -A
   git commit -m "Add [service name] to homelab"
   git push origin main
   ```
