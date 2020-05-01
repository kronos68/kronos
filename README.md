Tested on Kali linux, Parrot Os and Linux Mint, Can be used on Windows but you will have to install the Python-Interpreter and winpcap.exe.

Usage:

    - pip install -r requirements.txt
    
    
    - sudo chmod +x *
    
    
    - sudo python2 Arp_spoofer.py
    
    
       eg : target_ip >>> 192.168.43.83 // 192.168.10.32
            gateway >>> 192.168.43.1    // 192.168.10.1
            
            
    - don't forget to set your ARP tables.
    
    
        echo 1 > /proc/sys/net/ipv4/ip_forward
            
    - To stop the program just hit CTRL + C , and the ARP Tables in the victims device will be restored.
    
    
    
   
   Open up another terminal/tab and start the sniffer:
    
    Usage:
    
    
        - sudo python2 sniffer.py
        
        - interface >>> wlan0 // eth0 // ensp03.
        
        
        - Enter the Interface, the interface might differ from different linux distros, for windows, you can use the name of your
        
        
        wifi or ethernet adapter to use as the interface


