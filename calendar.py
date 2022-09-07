t=int(input())
for i in range(t):
    n=int(input())
    l=list(map(int,input().split()))
    d=8
    st=[6,13,20,27,7,14,21,28]
    for i in l:
        if i not in st:
            d=d+1
    print(d)