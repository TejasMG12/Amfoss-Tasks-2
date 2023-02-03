import re
pw="Abcdefgh1"
def strongpw(chk):
    chrchk= re.compile(r'[a-zA-Z]')
    digichk=re.compile(r'[0-9]')
    l1=chrchk.findall(chk)
    l2=digichk.findall(chk)
    f=0
    for e in l1:
        if e.isupper():
            f=1
            break
        
    if len(l1)>=8 and len(l2)>=1 and f==1:
        return True
    else:
        return False
    
print(strongpw(pw))    
