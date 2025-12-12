# ==========================================
# 📌 Module 1 — Multi-Threaded TCP Scanner
# ==========================================


import socket
import concurrent.futures

def scan_tcp_port(host, port, timeout=0.3):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(timeout)
            result = s.connect_ex((host, port))
            return port if result == 0 else None
    except:
        return None


def threaded_tcp_scan(host, ports, workers=200):
    open_ports = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as executor:
        results = executor.map(lambda p: scan_tcp_port(host, p), ports)
        for res in results:
            if res:
                open_ports.append(res)

    return open_ports
