import os
import sys
import re

new_name=""
if len(sys.argv)==2:
    new_name=sys.argv[1]

while new_name:
    folder=os.getcwd()
    count=0
    for filename in os.listdir(folder):
        if "renamer" in filename:
            continue
        src=f"{folder}/{filename}"
        if not os.path.isfile(src):
            continue
        count=count+1
        ext=""
        result=re.search(r'\.([a-zA-Z0-9]+)$', filename)
        if result:
            ext=ext+result.group(0)
        dest=f"{folder}/{new_name}{str(count)}"+ ext
        os.rename(src,dest)
    break


