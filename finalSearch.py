import pickle
import os
from sets import Set
ignore=['is','am','are','in','on','to']
f=open('indexing.pkl','rb')
cur_dir=os.getcwd()
indexes=pickle.load(f)
l,docid,di=indexes
f.close()
display=[]
query=raw_input("Enter the query to be searched\n")
query=list(Set(query.split()))
doclist={}
for word in query:
    if word in ignore:
        continue
    if word in di:
        for i in di[word]:
            if i in doclist:
                doclist[i]+=1
            else:
                doclist[i]=1
print doclist
for w in sorted(doclist, key=doclist.get, reverse=True):
  display.append(cur_dir+'\\search_files\\'+w)
  print w,doclist[w]
print display
if display==[]:
    print "No results found"
"""for adr in display:
    f=open(adr)
    for i in f:
        print i
    f.close()"""
