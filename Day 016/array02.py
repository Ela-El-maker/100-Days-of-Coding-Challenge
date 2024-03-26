import numpy as np

print('Numpy Version :- ',np.__version__)

arr = np.array([11,22,33,44,55,66])

print(arr)

print(type(arr))
# 0 Dimension array
arr1 = np.array(11)
print('0 Dimension array :- ',arr1)


# 1 Dimension array
arr2 = np.array([11,22,33,44,55])
print('1 Dimension array :- ',arr2)

# 2 Dimension array
arr3 = np.array([[1,2,3],[4,5,6]])
print('2 Dimension array :- ',arr3)

# 3 Dimension array
arr4 = np.array([[[1,2,3,4],[5,6,7,8]],[[11,22,33,44],[55,66,77,88]]])
print('3 Dimension array :- ',arr4)
