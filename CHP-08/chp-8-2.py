import pyinputplus as pyip
import time
mr=0
for i in range(10):
    print("What is",i,"*",i,"?")
    f=0        
    try:
        for j in range(3):
            res = pyip.inputNum(timeout=8)
            if res== i*i:
                print("Correct!")
                time.sleep(1)
                mr+=1
                f=0
                break
                
            else:
                print("Try again")
                f=1
    except :
        f=1
        time.sleep(1)
    if f==1:
        print("incorrect")
print("you got %s/10 questions right"%mr)
