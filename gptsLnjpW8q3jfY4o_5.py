
def Formula(n):
    def item(power,variable):
        result = ""
        if(power == 1):
            result = str(variable)
        elif (power > 1):
            result = str(variable) + "^" + str(power)
        return result
    def combination(l,r):
        result = ""
        r_factorial = 1
        n_factorial = 1
        n_minus_r_factorial = 1
        for i in range(1,r+1):
            r_factorial = r_factorial*i
        for p in range(1,l+1):
            n_factorial = n_factorial*p
        for x in range(l-r):
            n_minus_r_factorial = n_minus_r_factorial*(x+1)
        result = int(n_factorial/(r_factorial*n_minus_r_factorial))
        if result == 1:
            result = ""
        return result
    final_result = ""
    for i in range(abs(n)+1):
        final_result+= str(combination(abs(n),i)) + str(item(abs(n)-i,"a")) + str(item(i,"b"))
        if i < abs(n):
            final_result+= "+"
    if n == 0:
        final_result = "1"
    if n < 0:
        final_result = "1/(" + final_result + ")"
    return final_result

