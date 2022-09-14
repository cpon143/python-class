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

# ----------------------------------------------
# append()_add a single to the list
odd=[1,3,5]
odd.append(7)
print(odd)
# --------------------------
# odd.extend[9,11,13]
# print(odd)

# insert   
# delete=is used to delete items from list
# oddd=[1,3,5,7,11]
# # single items
# del oddd[1]
# print(oddd)
# -----------------------------------pop
even=[2,4,6,8]
even.remove(3)
even.pop(4)
# newwwwwwwwwwww

