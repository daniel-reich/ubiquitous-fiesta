
def countdown(operands, target):
​
    import itertools
​
    len_opands = len(operands)  
    len_optors = len(operands) - 1      
    optors = ['+', '-', '*', '//']
    lst_opands = list(itertools.permutations(operands, len_opands))
    lst_optors = list(itertools.product(optors, repeat = len_optors))
    
    for x in lst_opands:
        for y in lst_optors:
            if len_opands == 2:
                d = str(x[0]) + y[0] + str(x[1])
                if eval(d) == target:
                    return d
            elif len_opands == 3:
                d = str(x[0]) + y[0] + str(x[1]) + y[1] + str(x[2])
                if eval(d) == target:
                    return d
            elif len_opands == 4:
                d = str(x[0]) + y[0] + str(x[1]) + y[1] + str(x[2]) + y[2] + str(x[3])
                if eval(d) == target:
                    return d
            else:
                d = str(x[0]) + y[0] + str(x[1]) + y[1] + str(x[2]) + y[2] + str(x[3]) + y[3] + str(x[4])
                if eval(d) == target:
                    return d

