Usage:

    - pip install -r requirements.txt
    
    
    - chmod +x *
    
    
    - sudo ./Arp_spoofer.py
    
    
       eg : target_ip >>> 192.168.43.83
            gateway >>> 192.168.43.1  
            
            
    - don't forget to set your ARP tables.
    
        su
    
        echo 1 > /proc/sys/net/ipv4/ip_forward
            
    - To stop the program just hit CTRL + C , and the ARP Tables in the victims device will be restored.
    
    
    
   
   Open up another terminal/tab and start the sniffer:
    
    Usage:
    
    
        - sudo ./sniffer.py
        
        - interface >>> wlan0 // eth0 // ensp03 // wlp3s0b1
        
        
        - Enter the Interface, the interface might differ from different linux distros, for windows, you can use the name of your
        
        
        wifi or ethernet adapter to use as the interface


THE  QUITER  YOU  ARE  THE  MORE  YOU  ARE ABLE TO  HEAR.
