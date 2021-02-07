import requests,csv
import time 
import threading
from itertools import islice

HTTPResponse = requests.packages.urllib3.response.HTTPResponse
orig_HTTPResponse__init__ = HTTPResponse.__init__
def new_HTTPResponse__init__(self, *args, **kwargs):
    orig_HTTPResponse__init__(self, *args, **kwargs)
    try:
        self.peer_certificate = self._connection.peer_certificate
    except AttributeError:
        pass
HTTPResponse.__init__ = new_HTTPResponse__init__

HTTPAdapter = requests.adapters.HTTPAdapter
orig_HTTPAdapter_build_response = HTTPAdapter.build_response
def new_HTTPAdapter_build_response(self, request, resp):
    response = orig_HTTPAdapter_build_response(self, request, resp)
    try:
        response.peer_certificate = resp.peer_certificate
    except AttributeError:
        pass
    return response
HTTPAdapter.build_response = new_HTTPAdapter_build_response

HTTPSConnection = requests.packages.urllib3.connection.HTTPSConnection
orig_HTTPSConnection_connect = HTTPSConnection.connect
def new_HTTPSConnection_connect(self):
    orig_HTTPSConnection_connect(self)
    try:
        self.peer_certificate = self.sock.connection.get_peer_certificate()
    except AttributeError:
        pass
HTTPSConnection.connect = new_HTTPSConnection_connect

def scraper(no):
    rfile_name='phishtank'+str(no)+'.csv'
    wfile_name='pt_cert'+str(no)+'.csv'
    port=443
    write_file=open(wfile_name,mode='w')
    with open(rfile_name, newline='') as f:

        reader = csv.reader(f)
        next(reader,None)
        writer = csv.writer(write_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            hostname=row[1]
            if no%100==0:
                write_file.flush()
            print(hostname)
            try:
                r = requests.get(hostname, timeout=5)
                if not hasattr(r, 'peer_certificate'):
                    continue
            except KeyboardInterrupt:
                raise
            except:
                continue
            x509 = r.peer_certificate
            data=[]
            data.append(no)
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
            data.append(row[7])
            data.append(hostname)
            try:
                for i in range(x509.get_extension_count()):
                    if "crl" in x509.get_extension(i).__str__():
                        data.append(x509.get_extension(i).__str__().split("URI:")[-1])    
            except KeyboardInterrupt:
                raise
            except:
                data.append('N/A')
            writer.writerow(data)
            no+=1
    write_file.close()
    
 
if __name__=='__main__':
    start_time = time.time()
    scraper(21)
    print("--- %s seconds ---" % (time.time() - start_time))
        
        
