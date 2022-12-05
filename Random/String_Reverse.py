from tokenize import String


def StringReverse(str):
    str2 = ""
    for i in reversed(str):
        str2 += i
        print(str2)    



StringReverse("iamreversedstring")