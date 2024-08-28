import os
import sys

new_name=""
if len(sys.argv)==2:
    new_name=sys.argv[1]

while new_name:
    folder=os.getcwd()
    for count,filename in enumerate(os.listdir(folder)):
        if "renamer" in filename:
            continue
        src=f"{folder}/{filename}"
        dest=f"{folder}/{new_name}{str(count)}.jpg"
        os.rename(src,dest)
    break


