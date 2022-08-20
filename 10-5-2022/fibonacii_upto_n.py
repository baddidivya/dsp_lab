def fi(n):
   if n<=1:
       return n
   else:
        return(fi(n-1)+fi(n-2))
        y=fi(n-1)+fi(n-2)
        print(y)
n=int(input("enter n value"))
if n<=0:
    print("Invlid")
else:
    for i in range(n):
        fi(i)
