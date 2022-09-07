t= int(input())
for i in range(t):
    x =list (map(int, input().split()))
    if x[2]/x[0] < x[3]/x[1]: 
        print(-1)
    elif x[2]/x[0]== x[3]/x[1]:
        print(0)
    else:
        print(1)