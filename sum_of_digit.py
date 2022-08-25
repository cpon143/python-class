n=int(input("which digit do you want to sum"))
# 654321 to 123456
sum=0
while(n!=0):
    t=n%10
    sum=sum+t
    n=n//10
print(sum)
