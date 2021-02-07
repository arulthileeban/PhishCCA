import ssl,OpenSSL,csv
import time 
import threading
from itertools import islice

def scraper(start,end,no):
    print ("%s: %d" % ( "Thread name:",no))
    rfile_name='alexa-top1m.csv'
    wfile_name='alexa_certs'+str(no)+'.csv'
    port=443
    write_file=open(wfile_name,mode='w')
    with open(rfile_name, newline='') as f:
        reader = csv.reader(f)
        writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in islice(reader,start,end):
            if int(row[0])%10000==0:
                write_file.flush()
            hostname=row[1]
            hostname="www."+hostname
            try :
                conn = ssl.create_connection((hostname, port),timeout=2)
                if not conn:
                    continue
                context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
                if not context:
                    continue
                sock = context.wrap_socket(conn, server_hostname=hostname)
                if not sock:
                    continue    
            except KeyboardInterrupt:
                raise
            except:
                continue
            certificate = ssl.DER_cert_to_PEM_cert(sock.getpeercert(True))
            x509 = OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, certificate)
            data=[]
            data.append(row[0])
            data.append(x509.get_subject().C)
            data.append(x509.get_subject().O)
            data.append(x509.get_subject().CN)       
            data.append(x509.get_issuer().C)
            data.append(x509.get_issuer().O)
            data.append(x509.get_issuer().CN)
            data.append(x509.get_version())
            data.append(x509.get_serial_number())
            data.append(x509.get_signature_algorithm())
            data.append(x509.get_notAfter())
            data.append(x509.get_notBefore())
            try:
                for i in range(x509.get_extension_count()):
                    if "crl" in x509.get_extension(i).__str__():
                        data.append(x509.get_extension(i).__str__().split("URI:")[-1])    
            except KeyboardInterrupt:
                raise
            except:
                data.append('N/A')
            writer.writerow(data)
    write_file.close()
    
 
if __name__=='__main__':
    start_time = time.time()
    t1=threading.Thread(target=scraper,args=(1,249999,1,))
    t2=threading.Thread(target=scraper,args=(250000,499999,2,))
    t3=threading.Thread(target=scraper,args=(500000,749999,3,))
    t4=threading.Thread(target=scraper,args=(750000,1000000,4,))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("--- %s seconds ---" % (time.time() - start_time))
        
        
