import os
query=raw_input("Enter the query\n")
for root, dirs, files in os.walk(os.getcwd()):
    for i in files:
        f=open(i,"rb")
        for line in f:
            print line
        """if name==query:
            print "File found",name
        else:
            f=open(name)
            x=0
            for line in f:
                x+=1
                if query in line:
                    print query,"is is in",name,"at line no",x
                    print line
            f.close()"""
