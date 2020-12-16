from glob import glob
import os
import shutil
dirs=glob("*")
dirs.remove("create_ds.py")
dirs.remove("Other")
cwd=os.getcwd()+"/"
save_dir=cwd+"pages_r/"
ct=0
for i in dirs:
    pr_dir=cwd+i
    os.chdir(pr_dir)
    subdirs=glob("*/")
    fdata=[]
    for j in subdirs:
        os.chdir(pr_dir)
        try:
            data1=open(j+"index.txt").read()
            #print(os.getcwd())
            data2=data1.strip("https://").strip("http://").strip("www.")
            '''data3=data2.split("/")
            if len(data3)>1 and ".html" in data3:
                data3= '/'.join(data3[:-1])
            else:
                data3='/'.join(data3)
            #print()'''
            os.chdir(os.getcwd()+"/"+j)
            fdata=glob(data2)
            html_file=fdata[0]+"/index.html"
            if os.path.exists(html_file):
                #print(os.getcwd()+"/"+html_file)
                save_fname=''.join(c for c in i if c.isalpha())+str(j)[:-1]
                shutil.copyfile(os.getcwd()+"/"+html_file,save_dir+save_fname)              
                ct+=1#os.getcwd()+fdata[0]+"/index.html")
        except Exception as e:
            print(e)
            pass
        #if fdata!=[]:
        #    print(fdata)
print(ct)

