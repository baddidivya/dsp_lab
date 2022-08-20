def power(d,e):
    if e==0:
        return 1
    else:
        return d*power(d,e-1)
x=int(input("enter degit"))
y=int(input("enter exponent value"))
print(power(x,y))
