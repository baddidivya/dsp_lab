def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
y=int(input("Enter number find factorial"))
print(fact(y))
