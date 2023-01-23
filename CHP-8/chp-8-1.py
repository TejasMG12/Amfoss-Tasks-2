import pyinputplus as pyip
fnlst=[]
MENU={'wheat':10,'white':12,'sourdough':9,'chicken':25, 'turkey':30,
      'ham':40,'tofu':50,'cheddar':15, 'Swiss':17,'mozzarella':25,
      'mayo':10, 'mustard':12, 'lettuce':10,'tomato':5}
fnlst.append(pyip.inputMenu(['wheat', 'white','sourdough']))    
fnlst.append(pyip.inputMenu(['chicken', 'turkey','ham','tofu']))
print("Do you want cheese")
che= pyip.inputYesNo()
if che=='yes':
    fnlst.append(pyip.inputMenu(['cheddar', 'Swiss','mozzarella']))
print("Do you want mayo, mustard, lettuce or tomato.")
mmlt= pyip.inputYesNo()
if mmlt=='yes':
    fnlst.append(pyip.inputMenu(['mayo', 'mustard', 'lettuce' ,'tomato']))
print("How many snadwiches do you want")
nos=pyip.inputInt()
while nos<1:
    print("Please enter more than one")
    nos=pyip.inputInt()
price=0
for e in fnlst:
    price=MENU[e] + price
print("your total price is:",price * nos)
