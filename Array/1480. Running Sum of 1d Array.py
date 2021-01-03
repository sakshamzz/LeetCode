# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].

class Solution(object):
    def runningSum(self, nums):
        for i in range(len(nums)):
            if i is not 0:
                nums[i] += nums[i-1]
        return nums




obj = Solution()
resultArray = obj.runningSum([1,2,3,4])
print(resultArray)
