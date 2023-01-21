import random
fns=0
def lst():
    ans=0
    occ=0
    x=random.randint(0,1)
    for i in range(99):
        x,y= random.randint(0,1),x
        if x==y:
            occ +=1
        else :
            occ=0
        if occ >=6:
            ans +=1
            break
    return ans
for i in range (10000):
    fns += lst()
print("percentage of streaks %s%%"%(fns/100))
