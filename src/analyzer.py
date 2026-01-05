import re

def ip_address_analyzer():
    ip_set = set()
    http_set = set()
    ip_address_count = dict()
    http_code_count = dict()
    ip_pattern = r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}"
    http_status_pattern = r"\d{3}$"
    with open('server_log.txt', 'r') as f:
        
        for line in f:
            ip_address = re.search(ip_pattern, line)
            http_status = re.search(http_status_pattern, line)
            
            if ip_address:
                ip_address = ip_address.group()
                if ip_address not in ip_set:
                    ip_set.add(ip_address)
                else:
                    ip_address_count.setdefault(ip_address, 1)
                    ip_address_count[ip_address] += 1
            
            if http_status:
                http_status = http_status.group()
                if http_status not in http_set:
                    http_set.add(http_status)
                else:
                    http_code_count.setdefault(http_status, 1)
                    http_code_count[http_status] += 1
                
    with open('log_summary.txt', 'w') as f:
        f.write(f"---- IP Address Summary ---- \nIP Address      Count\n")
        for ip in ip_set:
            if ip in ip_address_count:
                f.write(f"{ip:15s} : {ip_address_count[ip]}\n")
            else:
                f.write(f"{ip:15s} : 1\n")
                
        f.write(f"\n\n---- HTTP Status Code Summary ---- \nStatus   Count\nCode\n")
        for http_code in http_set:
            if http_code in http_code_count:
                f.write(f"{http_code:6s} : {http_code_count[http_code]}\n")
            else:
                f.write(f"{http_code:6s} : 1\n")

ip_address_analyzer()
            