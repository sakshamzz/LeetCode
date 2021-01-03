# Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.

# A subarray is a contiguous subsequence of the array.

# Return the sum of all odd-length subarrays of arr.

class Solution:
    def sumOddLengthSubarrays(self, arr) -> int:        
        total = 0
        start = 1                  #start at odd number, increment by 2 to next odd number
        while start < len(arr)+1:
            for i in range(len(arr)):
                if len(arr[i:i+start]) == start:                       #when len == start == odd, you want to find sum of splice
                    total += sum(arr[i:i+start])
            start += 2
        print(total)    




sol = Solution()
sol.sumOddLengthSubarrays([1,4,2,5,3])      