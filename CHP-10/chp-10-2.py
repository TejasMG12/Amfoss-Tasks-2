import os
from pathlib import Path
import re , shutil
pth=(input("Enter the path:").strip("'\""))
ls=os.listdir(pth)
size=float(input("Enter size of file you want to search in mb"))*1000000
while len(pth)>5:
    for e in ls:
        pthfl=pth+"/"+e
        f=0
        if not(os.path.isdir(pthfl)):
            x= os.path.getsize(pthfl)
            f=1
        if f and x > size:
            print(pthfl)
    pth=str(Path(pth).parent)
    ls=os.listdir(pth)
