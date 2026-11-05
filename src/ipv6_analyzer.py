from scapy.all import IPv6

def analizar_ipv6(packet):
    ipv6 = packet[IPv6]
    output = "=============== IPv6 ===============\n"
    output += f"IP Origin        : {ipv6.src}\n"
    output += f"IP Destination   : {ipv6.dst}\n"
    output += f"Traffic Class    : {ipv6.tc}\n"
    output += f"Flow Label       : {ipv6.fl}\n"
    output += f"Next Header      : {ipv6.nh}\n"
    output += f"Hop Limit        : {ipv6.hlim}\n\n"
    return output
