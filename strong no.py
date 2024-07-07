n=int(input('enter a number'))
temp=n
sum=0
while n >0:
    digit=n%10
    fact=1
    print("Digit",digit)
    for i in range(1,digit+1):
        fact=fact*i
        print('Factorial',fact)
        sum=sum+fact
        n=n//10
    if sum==temp:
        print(temp,"is  string number")
    else:
        print(temp,"is not string number")
