import sys
n=int(sys.argv[1])
#n=5
#n=int(input("enter value:"))
a=2
output="prime"
while(a<(n-1)):
    if((n%a)==0):
        output="not prime"
        break
    else:
        a=a+1
print(output)
