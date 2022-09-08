# list is an orderd sequence
# notation [ ] ->
# fibnoci series
fib=[1,1,2,3,5,8,13,21]
# indexing
print(fib[6])

# slicing
# 2 to 5
print(fib[2:6])
print(fib[-6:-1])

# concatination
l1=[1,2,3]
l2=[4,5,6,l1]
l2
l1=[1,2,3,4]
print(l2)
l1[2]=25
print(l1)

# ---------------------unpacking of list
x1,x2,x3=[11,22,33]
print(x1,x2,x3)