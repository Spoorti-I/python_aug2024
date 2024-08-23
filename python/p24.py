#program to check a number is prime
number=int(input('enter the number to check whether it is prime'))
if number > 1:
    for i in range(2,int(number%2)+1):
        if number%2==0:
            print('number is prime number')
        else:
            print('number is not prime number')
else:
    print('number is not a prime number')
    

