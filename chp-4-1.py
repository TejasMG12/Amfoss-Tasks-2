def items(L):
    n=len(L)
    try:
        if n>2:
            print("'",end="")
            for e in range(0,n-2):
                print(L[e],",",end="")
            print(L[n-2],"and",L[n-1],".'")
        elif n==2:
            print("'",L[0],"and",L[1],"'")
        elif n==1:
            print("'",L[0],"'")
    except:
        print()
