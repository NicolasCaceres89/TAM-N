from scapy.all import ARP

def analizar_arp(packet):
    arp = packet[ARP]
    output = "=============== ARP ================\n"
    output += f"Hardware Type    : {arp.hwtype}\n"
    output += f"Protocol Type    : {arp.ptype}\n"
    output += f"Operation        : {arp.op}\n"
    output += f"MAC Origin       : {arp.hwsrc}\n"
    output += f"IP Origin        : {arp.psrc}\n"
    output += f"MAC Destination  : {arp.hwdst}\n"
    output += f"IP Destination   : {arp.pdst}\n"
    return output
