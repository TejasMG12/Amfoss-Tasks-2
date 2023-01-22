import re

inp="Todays date is 29/02/2100"
def checkdate(date):
    datere=re.compile(r'(\d\d)/(\d\d)/(\d\d\d\d)')
    dt=datere.search(date)
    day=int(dt.group(1))
    mnt=int(dt.group(2))
    year=int(dt.group(3))
    if (mnt==4 or mnt==6 or mnt==9 or mnt==11)and (day)>0 and (day)<=30:
        print(dt.group(),";its a valid date")
        return True
    elif (mnt==1 or mnt==3 or mnt==5 or mnt==12 or mnt==7 or mnt==8 or mnt==10 )and (day)>0 and (day)<=31:
        print(dt.group(),";its a valid date")
        return True
    elif mnt==2:
        if day==29 and year%4==0 and (not year%100==0 or year%400==0):
            print(dt.group(),";its a valid date")
            return True
        elif day<29 and day>0:
            print(dt.group(),";its a valid date")
            return True
        else:
            print(dt.group(),";its not a valid date")
            return False
    else:
        print(dt.group(),";its not a valid date")
        return False
    
        


        
