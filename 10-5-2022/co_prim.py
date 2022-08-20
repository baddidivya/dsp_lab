def gcd(a,b):
    if a<b:
        x=a%b
        if x==0:
            return b
        else:
            return gcd(a,x)
    else:
        x=b%a
        if x==0:
            return a
        else:
            return gcd(b,x)
a=int(input("Enter any value"))
b=int(input("enter any value"))
y=gcd(a,b)
if y==1:
    print("given number is co-prime")
else:
    print("given number is not a co-prime")
