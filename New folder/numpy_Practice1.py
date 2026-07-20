import numpy as np

# ==============================================================================
# 1. Create an Array
# ==============================================================================
# Practice:
# Create a NumPy array of 10 integers and print it.

arr=np.arange(11)
print(arr)

# ==============================================================================
# 2. Find Number of Dimensions
# ==============================================================================
# Practice:
# Create:
# - 1D array
# - 2D array
# - 3D array
#
# Print their dimensions.
arr=np.arange(1,11)
arr1=np.arange(10).reshape(-1,5)
arr2=np.arange(27).reshape(3,3,3)
print("1D array:",arr,arr.ndim)
print("2D array:",arr1,arr1.ndim)
print("3D array:",arr2,arr2.ndim)

# ==============================================================================
# 3. Find Shape of Array
# ==============================================================================
# Practice:
# Create a 4 × 5 array and print its shape.
arr=np.arange(20).reshape(4,5)
print(arr,arr.shape)

# ==============================================================================
# 4. Find Total Number of Elements
# ==============================================================================
# Practice:
# Create a 3 × 4 array.
#
# Print the total number of elements.
arr=np.arange(12).reshape(-1,4)
print(arr.size)

# ==============================================================================
# 5. Find Data Type
# ==============================================================================
# Practice:
# Create arrays of:
# - Integer
# - Float
# - String
#
# Print their datatype.
arr=np.arange(20,dtype=int)
arr1=np.arange(20,dtype=float).reshape(2,10)
arr2=np.arange(20).reshape(4,5)
arr2=arr2.astype(str)
print(arr.dtype)
print(arr1.dtype)
print(arr2.dtype)

# ==============================================================================
# 6. Find Memory Used by Each Element
# ==============================================================================
# Practice:
# Create an integer array.
#
# Print the memory used by one element.
arr=np.arange(20).reshape(4,5)
print(arr)
print(arr.itemsize)

# ==============================================================================
# 7. Check Array Flags
# ==============================================================================
# Practice:
# Create an array and print all flags.
print(arr.flags)

# ==============================================================================
# 8. Create Array of Zeros
# ==============================================================================
# Practice:
# Create:
# - Five zeros
# - 3 × 3 zeros
arr=np.zeros(5)
arr1=np.zeros((3,3))
print(arr)
print(arr1)

# ==============================================================================
# 9. Create Array of Ones
# ==============================================================================
# Practice:
# Create:
# - Ten ones
# - 4 × 2 ones
arr=np.ones(10)
arr1=np.ones((4,2))
print(arr)
print(arr1)

# ==============================================================================
# 10. Create Identity Matrix
# ==============================================================================
# Practice:
# Create identity matrices of:
# - 3 × 3
arr=np.eye(3)
arr1=np.eye(5)
print(arr)
print(arr1)
