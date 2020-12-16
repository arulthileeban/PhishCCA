import requests,csv
import time 
import threading
from itertools import islice

prefix="Dataset/"
def scraper(no):
    rfile_name=prefix+'pt_cert'+str(no)+'.csv'
    wfile_name=prefix+'pt_cert_mod'+str(no)+'.csv'
    port=443
    write_file=open(wfile_name,mode='w')
    with open(rfile_name) as f:
        reader = csv.reader(f)
        next(reader,None)
        writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            data=row[:12]
            if 'crl' in row[12]:
                crl=row[12]            
                crl=crl.replace("\n","")
                data.append(row[13])
                data.append(row[14])
            else:
                crl="N/A"                
                data.append(row[12])
                data.append(row[13])
            data.append(crl)
            writer.writerow(data)
    write_file.close()
    
 
if __name__=='__main__':
    start_time = time.time()
    scraper(1)
    scraper(2)
    print("--- %s seconds ---" % (time.time() - start_time))
        
        
