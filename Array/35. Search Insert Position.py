from tracemalloc import start


def searchInsert(nums,target):
    left, right = 0, len(nums) - 1
        
    while left <= right:
        middle = left + (right-left) // 2
        if nums[middle] == target: return middle
        if nums[middle] > target: right = middle - 1
        else: left = middle + 1
    return left


index = searchInsert([1,2,5,7,9],6)
print(index)