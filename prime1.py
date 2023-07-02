def prime_number(N):
    i=2
    while(i<=N):
        if(N%i)==0:
            N=N/i
        else:
            i=i+1

a=int(input("enter the number: "))
if prime_number(a):
    print("this is prime number:",a)
else:
    print("this is not a prime number:",a)
