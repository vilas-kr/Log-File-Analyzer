import faker

def log_file_generator():
    fake = faker.Faker()
    
    log_level = ['ERROR', 'WARNING', 'CRITICAL', 'INFO']
    
    with open("server_log.txt", "w") as f:
        for i in range(100):
            ip_address = fake.ipv4()
            datetime = fake.date_time().strftime(f"%d/%m/%Y:%H:%M:%S +0530")
            log = fake.random_element(log_level)
            desc = fake.sentence(nb_words=8)
            http_code = fake.http_status_code()
            f.write(f"{ip_address} {datetime} {log} {desc} {http_code}\n")
            
log_file_generator()

            
        
        
        
        

