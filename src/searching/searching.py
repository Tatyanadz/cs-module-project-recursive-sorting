# TO-DO: Implement a recursive implementation of binary search
def binary_search(arr, target, start, end):
    # Your code here
    mid = (start + end) // 2
    # base case is target == arr[mid]
    if mid >= 0 and target == arr[mid]:
        return mid

    # of arr[mid] is bigger than target then we need to set the end to the middle -1 (left side)
    if mid >= 0 and arr[mid] > target:
        return binary_search(arr, target, start, mid-1)
    # of arr[mid] is small than target then we need to set the end to the middle +1 (right side)

    if mid >= 0 and arr[mid] < target:
        return binary_search(arr, target, mid+1, end)
    else:
        return -1

# STRETCH: implement an order-agnostic binary search
# This version of binary search should correctly find 
# the target regardless of whether the input array is
# sorted in ascending order or in descending order
# You can implement this function either recursively 
# or iteratively
# def agnostic_binary_search(arr, target):
    # Your code here

