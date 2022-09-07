T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    chocolates = list(map(int, input().split()))

    out_ = (chocolates, M, N)
    print(out_)