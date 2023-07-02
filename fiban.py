n=int(input("enter the num:"))

def fib(n): 
        a=0
        b=1
        count=2
        print(a)
        print(b)
        while(count!=n):
                c=a+b
                print(c)
                a=b
                b=c
                count=count+1

def prime(n):
    a=2
    output="prime"
    while(a<(n-1)):
        if((n%a)==0):
            output="not prime"
            break
        else:
            a=a+1
    print(output)
    global p
    p = 10

prime(n)
fib(p)
