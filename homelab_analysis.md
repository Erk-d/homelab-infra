# Homelab Analysis & Troubleshooting Report

## Current Status
The homelab setup is currently unstable. While the server is reachable via SSH (`192.168.68.75`), the web services are failing to load.

## Root Cause Analysis
The primary issue is a **Docker version mismatch** on your server.

1.  **Symptom**: You received a `KeyError: 'ContainerConfig'` when running `docker-compose`.
2.  **Cause**: This error identifies that you are running an outdated version of **Docker Compose (v1.29.x)** (installed via `apt install docker-compose`). This old version cannot understand the container format created by the newer Docker Engine, causing it to crash.
3.  **Result**: 
    - Because `docker-compose` crashed, it failed to recreate the `bookstack` container (which we manually deleted).
    - It likely left the network stack in an inconsistent state, causing other containers (Vaultwarden, Plex) to become unreachable or effectively stopped.

## Configuration Review (`homelab-infra`)
I have reviewed your infrastructure files:
*   **`docker-compose.yml`**: The configuration is largely correct, but there is a **Port Conflict** with `adguardhome`.
    *   `npm` (Nginx Proxy Manager) binds ports `80` and `443`.
    *   `adguardhome` uses `network_mode: host`, which tries to grab port `80` for its Admin UI.
    *   **Conflict**: Only one service can hold port 80. This may prevent AdGuard or NPM from starting correctly.
*   **`services.yaml`**: Detailed configuration is good (hardcoded IP `192.168.68.75`), but likely points to ports that are currently closed due to the crash.

## Recommended Fix
We need to modernize the Docker installation on your server to support the deployment.

### Phase 1: Upgrade Docker Compose
We must replace the old `apt` version of `docker-compose` with the modern standalone version or plugin.

### Phase 2: Resolve Port Conflict
We should move AdGuard Home's web interface to a different port (e.g., `3000`) so it doesn't fight with Nginx Proxy Manager.

### Phase 3: Redeploy
Once the tools are fixed, we can run `docker-compose up -d` successfully to bring everything back online.
