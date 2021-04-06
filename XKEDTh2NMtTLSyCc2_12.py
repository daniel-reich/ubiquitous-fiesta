
def valid_credit_card(number):
    number = str(number)
    Sum = 0
    if len(number)%2 == 0: double = True
    else: double = False
    for i in range(0,len(number)):
        if double:
            addend = int(number[i])*2
            while len(str(addend))>1:
                addend = int(str(addend)[0]) +int(str(addend)[1])
            Sum+=addend
        else:
            Sum+=int(number[i])
        double= not double
    return(Sum%10 == 0)

