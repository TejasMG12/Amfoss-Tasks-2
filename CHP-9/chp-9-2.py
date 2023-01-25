#from pathlib import Path
pth=input("Enter path of file").strip("'\"")
while True:
    
    try:
        f1=open(pth)
        print(f1.read())
        break
    except IsADirectoryError:
        pth=input("Enter path of file").strip("'\"")
f1=open(pth)

ls=(f1.read()).split('\n')
f1.close()
for i,e in enumerate(ls):
    ls[i]=ls[i].split(' ')

for ele2 in ls:
    for ele in('ADJECTIVE', 'NOUN', 'ADVERB','VERB'):
        while ele in ele2:
            print("Enter an:",ele)
            x=input()
            ele2[ele2.index(ele)]=x
    for ele in('ADJECTIVE.', 'NOUN.', 'ADVERB.','VERB.'):
        while ele in ele2:
            print("Enter an:",ele)
            x=input()+"."
            ele2[ele2.index(ele)]=x
for e in ls:
    for ele in e:
        print(ele,end=' ')
    print()
f1.close()
