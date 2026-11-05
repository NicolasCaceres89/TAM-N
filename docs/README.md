# TAM-N

### Descripción
TAM-N (Traffic Analyzer & Monitoring Networks) es una herramienta de detección creada en 
Python usando Scapy, para describir diferentes tipos de paquetes, solo necesitas tu terminal 
CLI para ejecutarlo, con una sencilla interfaz de usuario y funciona guardado cada una de las 
salidas en un archivo de registro para análisis posterior.

### Objetivo
El objetivo de TAM-N, es la realizacion de un Sniffer para la materia de Programación de 
Aplicaciones de Red, siendo un proyecto para el analisis de paquetes y tramas, utilizadas 
comunmente para la comunicación entre dispositivos

Analizando Paquetes IP, Protocolos DNS, ARP, TCP y UDP... Para monitorear y analizar, todo
el trafico que fuye através de nuestro dispositivo.

### Documentación
#### Índice
- [Estructura](#estructura-proyecto-tam-n)
- [Uso Scapy Modulos](#uso-de-scapy-en-cada-modulo)

#### Estructura Proyecto TAM-N
```
.
├── docs
│   └── README.md
└── src
    ├── arp_analyzer.py
    ├── dns_analyzer.py
    ├── ethernet_analyzer.py
    ├── icmp_analyzer.py
    ├── ipv4_analyzer.py
    ├── ipv6_analyzer.py
    ├── logger.py
    ├── main.py                # orquestador del programa, donde se utilizan las funciones
    ├── net.py                 # agrega y reexporta las funciones de análisis
    ├── tcp_analyzer.py
    └── udp_analyzer.py

```

#### Uso de Scapy en Cada Modulo
```
-----------------------------------------------------------------------------------
| Módulo               |   Capa Scapy   |              Campos usados              |
|----------------------|----------------|-----------------------------------------|
| ethernet_analyzer.py | `Ether`        | `src`, `dst`, `type`                    |
| ipv4_analyzer.py     | `IP`           | `src`, `dst`, `ttl`, `proto`, `len`     |
| ipv6_analyzer.py     | `IPv6`         | `src`, `dst`, `hlim`, `nh`              |
| tcp_analyzer.py      | `TCP`          | `sport`, `dport`, `flags`, `seq`, `ack` |
| udp_analyzer.py      | `UDP`          | `sport`, `dport`, `len`                 |
| icmp_analyzer.py     | `ICMP`         | `type`, `code`                          |
| arp_analyzer.py      | `ARP`          | `op`, `psrc`, `pdst`, `hwsrc`, `hwdst`  |
| dns_analyzer.py      | `DNS`, `DNSQR` | `qd.qname`, `an`                        |
-----------------------------------------------------------------------------------
```
Para cada caso, se llamo directamente a cada capa de red en Scapy dentro de su ```<archivo>.py```
mediante ```from scapy.all import <layer>```. estos se concentraron en un solo archivo de python 
llamado ```net.py```.

```
# net.py actua unicamente como un agregador de funciones...
from ethernet_analyzer import analizar_ethernet
from ipv4_analyzer import analizar_ipv4
from ipv6_analyzer import analizar_ipv6
from icmp_analyzer import analizar_icmp
from arp_analyzer import analizar_arp
from udp_analyzer import analizar_udp
from dns_analyzer import analizar_dns
from tcp_analyzer import analizar_tcp
from logger import guardar_log 
```
Esto mantiene el ```main.py``` limpio para que solo funcione como un orquestador.

Tambien se hizo uso de la documentación oficial de Scapy, ademas de uno que otro recurso en PDF, 
o paginas de terceros, incluyendo el uso IA, para comprender ciertas caracteristicas que no eran
muy claras en la documentacion oficial.

#### Maquetación

