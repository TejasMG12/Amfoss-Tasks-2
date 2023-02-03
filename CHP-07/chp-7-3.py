import re
x=input("enter text:")
wts=input("enter what to strip:")
def Strip(string,inp):
    if inp=='':
        inp=' '
    len1=len(string)
    len2=len(inp)
    chk=re.compile('^' +inp)
    while chk.search(string)!= None and chk.search(string).group()== inp:
        string=string[len2::]
        len1=len(string)
        len2=len(inp)
        chk=re.compile('^' +inp)
    chk=re.compile(inp +'$')
    while chk.search(string)!= None and chk.search(string).group()== inp:
        string=string[0:len1-len2:]
        len1=len(string)
        len2=len(inp)
        chk=re.compile(inp+'$')
    print(string)
Strip(x,wts)
    
