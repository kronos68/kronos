Tested on Kali linux, Parrot Os and Linux Mint, Can be used on Windows but you will have to install the Python-Interpreter and winpcap.exe.

Usage:
    - pip install -r requirements.txt
    
    - chmod +x Arp_spoofer.py
    
    - python2 Arp_spoofer.py
    
       eg : target_ip >>> 192.168.43.83 // 192.168.10.32
            gateway >>> 192.168.43.1    // 192.168.10.1
            
    - don't forget to set your ARP tables.
    
        echo 1 > /proc/sys/net/ipv4/ip_forward
            
    - To stop the program just hit CTRL + C , and the ARP Tables in the victims device will be restored
