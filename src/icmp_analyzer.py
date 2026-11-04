from scapy.all import ICMP

def analizar_icmp(packet):
    icmp = packet[ICMP]
    output = "=============== ICMP ==============="
    output += f"Type        : {icmp.type}\n"
    output += f"Code        : {icmp.code}\n"
    output += f"Checksum    : {icmp.chksum}\n"
    return output
