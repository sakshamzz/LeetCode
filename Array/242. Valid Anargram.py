def ValidAnagram(s,t):
    y = MakeArr(s)
    z = MakeArr(t)
    return y == z

def MakeArr(j):
    arr = []
    for i in j:
        arr.append(i)
    arr.sort()
    return arr    

val = ValidAnagram("anagram","nagaram")
print(val)