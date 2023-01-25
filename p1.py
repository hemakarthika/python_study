def palin_prg(s):
    return s==s[::-1]

a=input("enter the string: ")


if palin_prg(a):
    print(a," is palindrome")
else:
    print(a," is not palindrome")
    
