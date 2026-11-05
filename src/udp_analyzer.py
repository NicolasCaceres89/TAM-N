from scapy.all import UDP

def analizar_udp(packet):
    udp = packet[UDP]
    output = "================ UDP ===============\n"
    output += f"Origin Port        : {udp.sport}\n"
    output += f"Destination Port   : {udp.dport}\n\n"
    return output
