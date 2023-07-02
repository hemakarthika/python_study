import sys
string=str(sys.argv[1])
str1=""
for i in string:
    str1=i+str1
print("the reverse order of string is: ",str1)
if(str1==string):
    print("the string %s is palindrome:" %(string) )
else:
    print("the string is not palindrome")

