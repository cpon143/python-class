days=int(input("Enter number of days"))
a=0.510
b=1
c=5
if days<=0:
    print("no fine")
elif days>=5 and days <=10:
    print("Rs",a)
elif days>=10 and days <=30:
    print("Rs",b)
else:
    print("Rs",c)

