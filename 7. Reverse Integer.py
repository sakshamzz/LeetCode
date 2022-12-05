def myFunc(x):
    number = x
    result = 0
    sign = [1,-1][x < 0]``
    while(number != 0):
        result = result*10 + ( number%10 )
        number =  int(number/10)
        print(number)


    return result * sign


x = myFunc(-531)
print(f'{x}') 