def collatz(number):
    if number%2==0:
        return number//2
    else:
        return 3 * number + 1
while True:
    
    try:
        n=int(input())
        while n!=1:
            n=collatz(n)
            print(n)
        break
    except ValueError:
        print("you must enter a integer")
 
