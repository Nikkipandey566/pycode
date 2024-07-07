n=int(input('enter a number'))
iterations=0
while iterations<100:
    total=0
    num=1
    while num >0:
        separate=num%10
        total=total+separate
        num=num//10
    num=total
    iterations=iterations+1
    if total==1:
        print('Magic Number')
        break
else:
    print('Not a Magic Number')
