def buildArray(arr,n):
    target = []
    result = []
    for i in range(1,n+1):
        if target != arr:
            target.append(i)
            result.append("Push")
            if i not in arr:
                target.pop()
                result.append("Pop")
    print(result)        

buildArray([1,2],4)