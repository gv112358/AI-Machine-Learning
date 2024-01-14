#sniffer in python
from scapy.all import *
from scapy.layers.inet import IP, TCP
from scapy.layers.inet import ETH_P_ALL
from scapy.all import bytes_hex
from scapy.layers.l2 import ARP
#from scapy.layers.tls.record import TLS
#import dbclient as db

#Questo codice genera tutti i vettori di numeri interi in base a
#f(N,K). Esempio f(5,10) da come output tutti i vettori di 5 numeri, la
#cui somma fa 10, es. [2,3,2,2,1]
f=lambda n,t:[k for k in product(range(t+1),repeat=n)if sum(k)==t]
from itertools import*
"""
for i in range(1,4):
    print(i)
    vettorePesi_globale = f(2, i)
    for vect in vettorePesi_globale:
        print(vect)

sys.exit()
"""

#dovete prendere la sequenza di bytes piu lunga dove i bytes sono tutti:
#0 1 2 3 4 5 6 7 8 9 a b c d e f

#46          2E
#97-122      61 - 7A
#48-57       30 - 39

#se vettore pesi == [1,0] target diventa target + 1, max_len -> max_len -1, target è la posizione di nomehost
#se vettore_pesi == [0,1] targett rimane target, max_len -> max_len -1 
#se vettore pesi == [1,1] target diventa target +1. max_len -> max_len - 2
#target = target + vettore_pesi[0] e max_len -> max_len - sum(vettore_pesi)
lunghezza =0
def check_nomehost(payload, inizio, len):
    if inizio < 2:
        return 0
    len_letto = bytes(payload)[inizio - 2] * 16 + bytes(payload)[inizio - 1]
    if len_letto==lunghezza:
       # print("okokok")
        return 1
    else:
        print("kokoko")
        return 0


def estrai_nome_host(payload):
    max_len = 0
    target = 0
    lunghezza = 0
    flag = 0
    posizione = 0
    inizio = 0
    for b in bytes(payload):
        if (0x30 <= b <= 0x39) or (b == 0x2E) or (0x61 <= b <= 0x7A) or (b == 0x2d) or (b == 0x5f):
            lunghezza += 1
            if flag == 0:
                flag = 1
                inizio = posizione
        else:
            if max_len < lunghezza:
                max_len = lunghezza
                target = inizio
            lunghezza = 0
            flag = 0
        posizione += 1

    ret = check_nomehost(payload, target, max_len)
    if ret == 1:
        return [target, max_len]
    print ("nome host sbagliato: ")
    print(bytes(payload)[target: target +max_len])
    target_new = 0
    max_len_new = 0
    for i in range(1,4):
        print(i)
        vettorePesi_globale = f(2, i)
        for vect in vettorePesi_globale:
            target_new = target + vect[0]
            max_len_new = max_len - vect[0] - vect[1]
            ret = check_nomehost(packet, target_new, max_len_new)
            if ret == 1:
                return [target_new, max_len_new]
    return [target, max_len]


    #check_nomehost(payload,target,max_len)
    #return [target, max_len]


def EstraiNomeHost(payload):
    for i in range(len(payload)):
        if int(bytes(payload)[i])==97 and int(bytes(payload)[i])<=122:
            print(bytes(payload)[i])


def myfilter(pkt):
    if pkt.haslayer(IP):
        if pkt[IP].src == '66.22.243.15' or pkt[IP].dst == '66.22.243.15':
            return 1
        if pkt[IP].src == '66.22.243.6' or pkt[IP].dst == '66.22.243.6':
            return 1
        if pkt[IP].proto == 17:
            return 1
        if pkt[IP].proto == 6:
            if pkt[TCP].dport == 443:
                if len(pkt[TCP].payload)>0 and bytes(pkt[TCP].payload)[0]==0x16 and bytes(pkt[TCP].payload)[5]==0x01:
                    ret = estrai_nome_host(pkt[TCP].payload)
                    print(bytes(pkt[TCP].payload)[ret[0]: ret[0] + ret[1]])
                    #hexdump(pkt[TCP].payload)
                    return 1
            if pkt[TCP].dport == 443:
                return 1
                #print(pkt[TCP].payload[0:6])
                if len(pkt[TCP].payload) >0 and bytes(pkt[TCP].payload)[0]==0x16 and bytes(pkt[TCP].payload)[5]==0x01:
                    #n1 = int(bytes(pkt[TCP].payload)[0x92])
                    #n2 = int(bytes(pkt[TCP].payload)[0x93])
                    #n3 = n1*16 + n2
                    #print(bytes(pkt[TCP].payload)[148 : 148 + n3])
                    #hexdump(pkt[TCP].payload)
                    ret = estrai_nome_host(pkt[TCP].payload)
                    print(bytes(pkt[TCP].payload)[ret[0]: ret[0] + ret[1]])
                    return 1
    return 1



def print_eth_layer(pkt):
    if myfilter(pkt)==1:
        return

    pkt_hex = bytes_hex(pkt)
    #print(pkt_hex[24])
    mac_dst = str(pkt_hex[0:12])
    mac_src = str(pkt_hex[12:24])
    eth_type = str(pkt_hex[24:28])
    #print(pkt_hex[0:28])
    print("MAC DST:" + mac_dst + " MAC SRC: " + mac_src + " ETH TYPE: " + eth_type)
    if eth_type == "b'0800'":
        print_ip_layer(pkt)
    elif eth_type == "b'0806'":
        print_arp_layer(pkt)
    elif eth_type == "b'8100'":
        print_eee_layer(pkt)
    elif eth_type.lower() == "b'86dd'":
        print_ipv6_layer(pkt)
    else:
        print_raw_layer(pkt)


def print_ip_layer(packet):
    ip_layer = "IP_SRC: " + packet[IP].src + " IP_DST: " + packet[IP].dst + " proto:" + str(
        packet[IP].proto) + " len:" + str(
        packet[IP].len) + " ttl:" + str(packet[IP].ttl) + " ihl:" + str(packet[IP].ihl)
    print(ip_layer)
    if packet[IP].proto==6:
        print_tcp_layer(packet)



def print_arp_layer(pkt):
        if pkt[ARP].op == 1: #who-has (request)
            print(f"ARP Request: {pkt[ARP].psrc} is asking about {pkt[ARP].pdst}")
        if pkt[ARP].op == 2:  # is-at (response)
            print(f" ARP Response: {pkt[ARP].hwsrc} has address {pkt[ARP].psrc}")

def print_eee_layer(packet):
    print("Da fare 2")

def print_ipv6_layer(packet):
    print("Da fare 3")

def print_raw_layer(packet):
    print(packet[0:min(60,len(packet))])


def print_tcp_layer(packet):
    tcp_layer = "TCP_SRC: " + str(packet[TCP].sport) + " TCP_DST: " + str(packet[TCP].dport) + " PL:" + \
                str(packet[TCP].dataofs) + " " + str(packet[TCP].flags) + " " + str(packet[TCP].options) + " " + str(packet[TCP].reserved)

    print(tcp_layer)


    #handle_tls_packet(packet)
    hexdump(packet[TCP].payload)



def handle_tls_packet(pkt):

    pkt_hex = bytes_hex(pkt)
    start_tls = 14*2 + (pkt[IP].ihl*4)*2 + 20*2
    tls_len = (pkt[IP].len -  (pkt[IP].ihl*4) - 20)*2

    ii = 0
    while((ii<tls_len - 16*2)):
        print(ii/2,pkt_hex[start_tls + ii:start_tls + ii+32])
        ii += 32
    print(ii/2,pkt_hex[start_tls + ii:start_tls +tls_len])

    #print(pkt[TLS].len)
    return


    if pkt.haslayer(Raw):
        b = bytes(pkt[Raw].load)

        if b[0] == 0x16:
            version =  int.from_bytes(b[1:3], 'big')
            message_len = int.from_bytes(b[3:5], 'big')
            handshake_type = b[5]
            handshake_length = int.from_bytes(b[6:9], 'big')

            print("v = ", version, " len = ", message_len, " htype =", handshake_type
            , "hlen =", handshake_length)

            if handshake_type == 11:
                # never happens - Why?
                certs_len = int.from_bytes(b[7:11], 'big')
                print("cert_len=" + certs_len)





def process_packet(packet):
    #print("Ho ricevuto un pkt")

    #pkt_hex = bytes_hex(packet)
    #print(pkt_hex[0:28])
    print_eth_layer(packet)


"""
print("Inizio programma gestione sniffer.")
cur = db.connect()
if cur is None:
	print("Errore connessione al DB")
	exit()
"""

#La wifi è en0
#sniff(iface="en4",filter="arp or ip", prn=process_packet)
sniff(iface="enp4s0", filter="ip", prn=process_packet)