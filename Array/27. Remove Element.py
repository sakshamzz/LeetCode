from os import remove


def removeElement(nums, val):
    res = 0
    for i in range(len(nums)):
        if nums[i] == val:
            for j in reversed(range(len(nums))):
                if j > i:
                    if nums[j] == val:
                        j = j - 1
                    else:
                        nums[j],nums[i] = nums[i],nums[j]
                        res = res + 1
                        break
                else: 
                    break
        else:
            res = res + 1
    return res           
        


x = removeElement([0,1,2,2,3,0,4,2],2)    
print(x)