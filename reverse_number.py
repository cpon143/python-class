n=int(input("which number do you want to reverse"))
# 654321 to 123456
rev=0
while(n!=0):
    t=n%10
    rev=rev*10+t
    n=n//10
print(rev)
