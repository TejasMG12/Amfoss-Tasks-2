import os
from pathlib import Path
import re , shutil
pth=(input("Enter the path:").strip("'\""))
ext=input("Enter extension you want to copy")
ls=os.listdir(pth)
if ext[0]!=".":
    ext="."+ext
try:
    os.mkdir("Copy-Folder")
    x=Path("Copy-Folder")

except:
    x=Path("Copy-Folder")
while len(pth)>5:
    for e in ls:
    
        if (Path(e).suffix)==ext:
        
            pthfl=pth+"/"+e
            shutil.copy(pthfl ,x)
    pth=str(Path(pth).parent)
    ls=os.listdir(pth)
