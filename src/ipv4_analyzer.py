from scapy.all import IP

def analizar_ipv4(packet):
    ipv4 = packet[IP]
    output = "=============== IPv4 ===============\n"
    output += f"IP Origin        : {ipv4.src}\n"
    output += f"IP Destination   : {ipv4.dst}\n"
    output += f"TTL              : {ipv4.ttl}\n"
    output += f"Protocol         : {ipv4.proto}\n\n"
    return output
