import os,threading,csv
from itertools import islice
from fake_useragent import UserAgent
import subprocess,time
def scraper(start,end):
    f=open("../phishtank1_21.csv","r")
    rf=csv.reader(f)
    ct=start
    for j in islice(rf,start,end):
        i=j[1]
        t=j[-1]
        if t=="Other":
            continue
        t=''.join(c for c in t if c.isalpha())+str(ct)
        ct+=1
        url=i.replace("\n","")
        try:
            #req = urllib.request.Request(url,data=None, headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'})
            #response = urllib.request.urlopen(req,timeout=5)
            #content = response.read()
            #f = open(t, 'w' )
            #f.write( content )
            #f.close()
            #s=i.replace("\n","").strip("https://").strip("http://").split("/")[0]
            #cmd="wget -nc -nv --no-check-certificate --tries=2 -O "+t+" "+"\""+url+"\""
            #os.system(cmd)
            #ua=UserAgent()
            #os.spawnl(os.P_NOWAIT,cmd)
            arg=["wget","-nc","-nv","--no-check-certificate","--tries=2","-O",t,url]
            subprocess.Popen(arg)
            time.sleep(2)
        except:
            pass
        print(ct)

if __name__=="__main__":
    os.chdir(os.getcwd()+"/pages_r")
    t1=threading.Thread(target=scraper,args=(1,3000))
    t2=threading.Thread(target=scraper,args=(3001,6000))
    t3=threading.Thread(target=scraper,args=(6001,9000))
    t4=threading.Thread(target=scraper,args=(9001,12250))
    t5=threading.Thread(target=scraper,args=(12251,15740))
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t5.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    t5.join()

