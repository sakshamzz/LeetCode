class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False
           




result =  Solution()
value = result.isPalindrome(545)
print(value)