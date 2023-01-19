pos=[]
pices=['wpawn', 'wknight', 'wbishop', 'wrook',
       'wqueen', 'wking','bpawn', 'bknight', 'bbishop',
       'brook', 'bqueen','bking']
for i in range(97,105):
    for j in range(1,9):
        pos.append(str(j)+chr(i))
def isValidChessBoard(CB):
    c=True
    
    if 'bking'not in CB.values() or 'wking' not in CB.values():
        c= False

    else:
        for po,pi in CB.items():
            if pi not in pices:
                c=False
            
            elif po not in pos:
                c=False
                 
            
    return c
che= {'1h': 'bking', '6c': 'wqueen',
      '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(che))
