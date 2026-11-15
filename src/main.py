# ==============================
# SNIFFER BASE - Programación de Aplicaciones de Redes
# ==============================

from scapy.all import *
from net import *
from datetime import datetime
import os
import time

contador = 0

# ==============================
# FUNCIÓN PRINCIPAL
# ==============================

def analizar_paquete(packet):
    global contador
    contador += 1
    
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_texto = f"\n[{timestamp}]\n"

    if packet.haslayer(Ether):
        log_texto += analizar_ethernet(packet)

    if packet.haslayer(IP):
        log_texto += analizar_ipv4(packet)

    if packet.haslayer(UDP):
        log_texto += analizar_udp(packet)

    if packet.haslayer(DNS):
        log_texto += analizar_dns(packet)

    if packet.haslayer(IPv6):
        log_texto += analizar_ipv6(packet)

    if packet.haslayer(ARP):
        log_texto += analizar_arp(packet)

    if packet.haslayer(ICMP):
        log_texto += analizar_icmp(packet)

    if packet.haslayer(TCP):
        log_texto += analizar_tcp(packet)

    log_texto += "-" * 50 + "\n"

    guardar_log(log_texto)
    print(f"\rCapturando paquetes... [{contador}]", end="", flush=True)
    

def main():
    os.system("clear")
    print("=== SNIFFER INICIADO ===")
    print(f"Los logs se guardan en: {os.path.abspath('log.txt')}")
    print("Presione Ctrl+C para detener\n")

    filtros_validos = {
        "tcp": "tcp",
        "udp": "udp",
        "icmp": "icmp",
        "arp": "arp",
        "dns": "port 53",
        "ipv6": "ip6",
        "ipv4": "ip"
    }

    filtro_usuario = input("Ingrese filtro (tcp, udp, icmp, arp, dns, ipv4, ipv6 o vacío): ").lower()
    print("")

    if filtro_usuario == "":
        sniff(prn=analizar_paquete, store=False)
    else:
        if filtro_usuario in filtros_validos:
            sniff(filter=filtros_validos[filtro_usuario],
                  prn=analizar_paquete,
                  store=False)
        else:
            print("Filtro no válido. Ejecutando sin filtro.")
            sniff(prn=analizar_paquete, store=False)


if __name__ == "__main__":
    main()
