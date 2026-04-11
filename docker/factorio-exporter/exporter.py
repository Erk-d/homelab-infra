#!/usr/bin/env python3
import os
import re
import time
import logging
from prometheus_client import start_http_server, Gauge, Info

logging.basicConfig(level=logging.INFO, format='%(asctime)s %(levelname)s %(message)s')
log = logging.getLogger(__name__)

RCON_HOST     = os.environ.get('RCON_HOST', 'factorio')
RCON_PORT     = int(os.environ.get('RCON_PORT', 27015))
RCON_PASSWORD = os.environ.get('RCON_PASSWORD', '')
INTERVAL      = int(os.environ.get('SCRAPE_INTERVAL', 15))

server_up      = Gauge('factorio_server_up',           '1 if server is reachable via RCON')
players_online = Gauge('factorio_players_online',      'Number of players currently online')
game_time_secs = Gauge('factorio_game_time_seconds',   'Current game time in seconds')
server_version = Info('factorio_server',               'Factorio server version')

def parse_player_count(response):
    match = re.search(r'\((\d+)\)', response)
    return int(match.group(1)) if match else 0

def parse_time(response):
    days = 0
    day_match = re.search(r'(\d+)\s+day', response)
    if day_match:
        days = int(day_match.group(1))
    t = re.search(r'(\d+):(\d+):(\d+)', response)
    if t:
        return days * 86400 + int(t.group(1)) * 3600 + int(t.group(2)) * 60 + int(t.group(3))
    return 0

def collect():
    try:
        from factorio_rcon import RCONClient
        client = RCONClient(RCON_HOST, RCON_PORT, RCON_PASSWORD)

        count = parse_player_count(client.send_command('/players online'))
        players_online.set(count)

        game_time_secs.set(parse_time(client.send_command('/time')))

        ver = client.send_command('/version').strip()
        server_version.info({'version': ver})

        server_up.set(1)
        log.info(f'OK — players={count} version={ver}')

    except Exception as e:
        log.error(f'Scrape failed: {e}')
        server_up.set(0)
        players_online.set(0)

if __name__ == '__main__':
    log.info(f'Factorio exporter starting on :9200, connecting to {RCON_HOST}:{RCON_PORT}')
    start_http_server(9200)
    while True:
        collect()
        time.sleep(INTERVAL)
