def printTable(tbl):
    bnl=[]
    for i in range(len(tbl)):
        LS=len(tbl[i][0])
        for j in tbl[i]:
            if len(j)>LS:
                LS= len(j)
        bnl.append(LS)

    lstr1= len(tbl[0])
    lstr2=len(tbl)
    print(lstr1,lstr2)
    for x in range(0,lstr1):
        print("|",end="")
        for j in range(0,lstr2):
            print(tbl[j][x].rjust(bnl[j]),"|",end=" ")
        

        print()

print("ok")
    
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]
printTable(tableData)
