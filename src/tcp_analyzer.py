from scapy.all import TCP

def analizar_tcp(packet):
    tcp = packet[TCP]
    output = "================ TCP ===============\n"
    output += f"Origin Port        : {tcp.sport}\n"
    output += f"Destination Port   : {tcp.dport}\n"
    output += f"Sequence           : {tcp.seq}\n"
    output += f"Acknowledgement    : {tcp.ack}\n"
    output += f"Offset             : {tcp.dataofs}\n"
    output += f"Flags              : {tcp.flags}\n"
    output += f"Window Size        : {tcp.window}\n\n"
    return output
