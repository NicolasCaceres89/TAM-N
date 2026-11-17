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
- [Uso Scapy Modulos](#uso-de-scapy-en-cada-módulo)
- [Maquetación](#maquetación)
- [Instalación](#instalación-tam-n)
- [Ejecución](#ejecución)

#### Estructura Proyecto TAM-N
```
.
├── docs
│   └── README.md
├── install.sh
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

#### Uso de Scapy en Cada Módulo
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
- Vista inicial.
```
=== SNIFFER INICIADO ===
Los logs se guardan en: /mnt/HomeOne/Projects/TAM-N/log.txt
Presione Ctrl+C para detener

Ingrese filtro (tcp, udp, icmp, arp, dns, ipv4, ipv6 o vacío): 

```

- Capturando paquetes.
```
=== SNIFFER INICIADO ===
Los logs se guardan en: /mnt/HomeOne/Projects/TAM-N/log.txt
Presione Ctrl+C para detener

Ingrese filtro (tcp, udp, icmp, arp, dns, ipv4, ipv6 o vacío): tcp

Capturando paquetes... [n]    #n es el numero de paquetes capturados
```

- Datos del Paquete en log.txt.
```
=============== [Type Package] ===============
[data-type]        : [value]
...
```

Los Paquetes capturados se guardan en ```~/.local/state/tamn/log.txt```

#### Instalación TAM-N

##### Requisitos
- Python 3.8 o superior
- Permisos de administrador (capturar tráfico requiere root)

##### Pasos
```bash
$ git clone https://github.com/NicolasCaceres89/TAM-N.git
$ cd TAM-N
$ chmod +x install.sh
$ ./install.sh
```
Se creo un Script de Bash para generar un ejecutable con todos los permisos necesarios para el 
funcionamiento de TAM-N. 

*Nota:* Se notifica que el uso de sudo es unicamente para brindar los permisos
para poder capturar el trafico de red, sin que tengan la necesidad de ejecutar el ejecutable con
sudo.

##### Ejecución
Para utilizar TAM-N Sniffer, solo tendra que ejecutar:

```bash
$ ./tamn
```

