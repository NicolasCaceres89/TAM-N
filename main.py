# ==============================
# SNIFFER BASE - Programación de Aplicaciones de Redes
# ==============================

from scapy.all import *
from datetime import datetime

# ==============================
# FUNCION ETHERNET
# ==============================
def analizar_ethernet(packet):
    print("Hola estoy escaneando Ethernet")
    return ""

# ==============================
# FUNCION IPv4
# ==============================
def analizar_ipv4(packet):
    print("Hola estoy escaneando IPv4")
    return ""

# ==============================
# FUNCION UDP
# ==============================
# def analizar_udp():

# ==============================
# FUNCION DNS
# ==============================
# def analizar_dns():

# ==============================
# FUNCION IPv6
# ==============================
# def analizar_ipv6():

# ==============================
# FUNCION ARP
# ==============================
# def analizar_arp():

# ==============================
# FUNCION ICMP
# ==============================
# def analizar_icmp():

# ==============================
# FUNCION TCP
# ==============================
# def analizar_tcp():

# ==============================
# FUNCIÓN PRINCIPAL
# ==============================

def analizar_paquete(packet):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_texto = f"\n[{timestamp}]\n"
    print("\n====================================")
    print("Paquete capturado:", timestamp)

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


def main():
    print("=== SNIFFER INICIADO ===")
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
