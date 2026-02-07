
import socket
import concurrent.futures
from datetime import datetime

# Target Configuration
BASE_IP = "192.168.68."
START_RANGE = 1
END_RANGE = 254
PORTS_TO_SCAN = [22, 80, 81, 443, 3001, 6875, 7575, 8080, 8384, 9000, 9443]

def scan_port(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5) # Short timeout
    result = sock.connect_ex((ip, port))
    sock.close()
    if result == 0:
        return port
    return None

def scan_host(ip):
    open_ports = []
    # Check if host is up first with a quick ping-like check on common ports
    # Or just scan all ports directly since the list is short
    for port in PORTS_TO_SCAN:
        if scan_port(ip, port):
            open_ports.append(port)
    
    if open_ports:
        return ip, open_ports
    return None

def main():
    print(f"Scanning {BASE_IP}1 to {BASE_IP}{END_RANGE}...")
    start_time = datetime.now()
    
    found_hosts = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=50) as executor:
        futures = {executor.submit(scan_host, f"{BASE_IP}{i}"): i for i in range(START_RANGE, END_RANGE + 1)}
        
        for future in concurrent.futures.as_completed(futures):
            result = future.result()
            if result:
                ip, ports = result
                print(f"[FOUND] {ip} | Open Ports: {ports}")
                found_hosts.append((ip, ports))

    end_time = datetime.now()
    duration = end_time - start_time
    print(f"\nScan completed in {duration}")
    
    if found_hosts:
        print("\nPossible Candidates:")
        for ip, ports in found_hosts:
            confidence = "Low"
            if 22 in ports: confidence = "Medium (SSH Open)"
            if 81 in ports or 9443 in ports or 7575 in ports: confidence = "High (Homelab Ports)"
            
            print(f"  - {ip}: {ports} [{confidence}]")
    else:
        print("\nNo hosts found with the specified ports open.")

if __name__ == "__main__":
    main()
