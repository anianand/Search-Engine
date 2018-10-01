import pickle
import os
cur_dir=os.getcwd()
search_dir=cur_dir+"\search_files"
#print search_dir
l=[]
x=0
docid={}
di={}
for files in os.walk(search_dir):
    l=files[2]
for i in l:
    docid[i]=x
    x+=1
for files in l:
    #print files
    f=open("./search_files/"+files,"r")
    for line in f:
        x=line.strip().split()
        for i in x:
            if i in di:
                if files not in di[i]:
                    di[i].append(files)
            else:
                di[i]=[]
                di[i].append(files)
    f.close()
#print di
indexes=[l,docid,di]
f=open('indexing.pkl','wb')
pickle.dump(indexes,f)
f.close()
