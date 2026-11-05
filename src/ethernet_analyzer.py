from scapy.all import Ether

def analizar_ethernet(packet):
    eth = packet[Ether]
    output = "============= Ethernet =============\n"
    output += f"MAC Origin      : {eth.src}\n" 
    output += f"MAC Destination : {eth.dst}\n"
    output += f"Type            : {hex(eth.type)}\n\n"
    return output
