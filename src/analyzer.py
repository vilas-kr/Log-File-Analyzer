import re

def ip_address_analyzer():
    ip_set = set()
    ip_address_count = dict()
    pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    with open('server_log.txt', 'r') as f:
        
        for line in f:
            ip_address = re.search(pattern, line)
            
            if ip_address:
                ip_address = ip_address.group()
            else:
                continue
                
            if ip_address not in ip_set:
                ip_set.add(ip_address)
            else:
                ip_address_count.setdefault(ip_address, 1)
                ip_address_count[ip_address] += 1
            
    with open('log_summary.txt', 'a') as f:
        f.write(f"---- IP Address Summary ---- \nIP Address      Count\n")
        for ip in ip_set:
            if ip in ip_address_count:
                f.write(f"{ip:15s} : {ip_address_count[ip]}\n")
            else:
                f.write(f"{ip:15s} : 1\n")
                


ip_address_analyzer()
            