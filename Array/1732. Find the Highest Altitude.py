def HigestAltitude(gain):
    max = gain[0] if gain[0] > 0 else 0
    for i in range(1,len(gain)):
        gain[i] = gain[i]+gain[i-1]
        max = gain[i] if max < gain[i] else max
    return max    



result = HigestAltitude([52,-91,72])    
print(result)
