import numpy as np
# 1D array
arr=np.array([1,2,3,4])
print(arr)
print(type(arr))
print(np.__version__)

print(1111111111)

# --------------------------------
# 2D array

arr2=np.array([[1,2,3,],[4,5,6]])
print(arr2)
print(22222222222222222)
# ---------------------------------
# 3D array
arr3=np.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12,]]])
print(arr3)
print("For dimention checking")
print(arr3.ndim)
print(333333333333333333)
# -----------------------------------
# 5 D array
arr5=np.array([[[[[1,2,3]]]]])
print(arr5)
print("Dimention of this array")
print(arr5.ndim)

# ------------------------------------
# 6 D array
arr6=np.array([1,2,3,4,5,6],ndmin=32)
print(arr6)
print(arr6.ndim)

# ------------------------------------
#  Access the array element
print("Accessing array")
arr11=np.array([1,2,3,4,5,6])
print(arr11[0])
print(arr11[-1])
print(arr11[0]+arr11[3])