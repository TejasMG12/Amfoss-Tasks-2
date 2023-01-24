#from pathlib import Path
f1=open('chp9text')
print(f1.read())
f1=open('chp9text')

ls=(f1.read()).split('\n')
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
