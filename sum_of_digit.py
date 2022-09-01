n=int(input("which digit do you want to sum"))
# 654321 to 123456
sum=0
while(n!=0):
    t=n%10
    sum=sum+t
    n=n//10
print(sum)


def add_digit(a:int):
    sum=0
    while(a!=0):
        t=a%10
        sum=sum+t
        a=a//10
    print(sum)
a=int(input("which digit do you want to sum"))
add_digit(a)

