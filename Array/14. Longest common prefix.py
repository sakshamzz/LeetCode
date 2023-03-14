
def longestCommonPrefix(arr):
    #base condition
    if len(arr) == 0:
        return ""
    # variable to store longest prefix
    longestStreak = ""

    # find shortest length of word, because prefix can not be 
    # greater than it's length O(n)
    strLength = len(arr[0])
    for i in arr:
        strLength = min(strLength,len(i))

    # iterate over shortest word O(n)
    for i in range(0,strLength):

        current = arr[0][i]  

        # go char by char for every element in arr. O(n^2)
        # ex: for 'f' in first element check if it exists in every other element at given index.
        for k in range(len(arr)):
            # if that element does not exists, return longestprefix
            if arr[k][i] != current:
                return longestStreak
        
        # only if character is present in  every other element, append it to longestStreak variable
        longestStreak += current    
      

pref = longestCommonPrefix(["flower","flow","flight"])
print(pref)