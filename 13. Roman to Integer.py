class Solution:
    def romanToInt(self, s: str) -> int:
        result = 0
        switcher = {

            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        for i in s:
            result += switcher.get(i)

        return result
           




obj =  Solution()
value = obj.romanToInt('IX')
print(value)