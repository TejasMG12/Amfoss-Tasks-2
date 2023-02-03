import os
from pathlib import Path
import re
pth=input("Enter the path:").strip("'\"")
regex=re.compile(input("Enter a regular expression:"))
ls=os.listdir(pth)
for e in ls:
    
    if (Path(e).suffix)=='.txt':
        
        pthfl=pth+"/"+e
        f1=open(pthfl)
        sch=regex.findall(f1.read())
        print(f"In {e}:",sch)
