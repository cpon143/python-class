from re import I


m=int(input("Enter the value of m less then n"))
n=int(input("Enter the value of n greater then m"))

count=0
for i in range(m,n):
    if(i%2==0):
        print(i)
        count=count+1
print("Total even number", count)
 
