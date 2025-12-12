from core.tcp_scanner import threaded_tcp_scan
from core.udp_scanner import scan_udp_port
from core.service_detect import detect_service
from core.banner_grabber import grab_banner
from core.vulnerability_checks import basic_vulnerability_checks
from utils.logger import setup_logger

log = setup_logger()

def start_scan(host):
    ports = range(1, 1025)

    log.info(f"Starting scan on {host}")
    tcp = threaded_tcp_scan(host, ports)

    report = []

    for port in tcp:
        service = detect_service(port)
        banner = grab_banner(host, port)
        vulns = basic_vulnerability_checks(port, banner or "")

        row = [host, port, service, banner]
        report.append(row)

        log.info(f"Open {port} - {service} - {banner} - {vulns}")

    return report
