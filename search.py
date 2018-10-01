import os
file_name = raw_input() #file to be searched
cur_dir = os.getcwd() # Dir from where search starts can be replaced with any path
"""while True:
    parent_dir = os.path.dirname(cur_dir)
    if parent_dir==cur_dir:
        break
    else:
        cur_dir=parent_dir"""
ans={}
while True:
    file_list = os.listdir(cur_dir)
    parent_dir = os.path.dirname(cur_dir)
    for i in file_list:
        if file_name in i:
            ans[i]=cur_dir
    if cur_dir == parent_dir: #if dir is root dir
        break
    else:
        cur_dir = parent_dir
if ans=={}:
    print "No matches found"
else:
    for i in ans:
        print "File ",i,"at location",ans[i]