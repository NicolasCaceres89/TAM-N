from scapy.all import DNS

def analizar_dns(packet):
    dns = packet[DNS]
    output = "=============== DNS ================\n"
    if dns.qd: 
        url = dns.qd.qname.decode(errors="replace").rstrip(".")
        output += f"Query    : {url}\n"
    return output
