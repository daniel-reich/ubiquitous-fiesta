
def postfix(expression):
    exp_list = expression.split()
    while len(exp_list) > 1:
        for k, v in enumerate(exp_list):
            if v in "/*-+":
                result = eval(exp_list[k-2] + v + exp_list[k-1])
                exp_list[k] = str(int(result))
                del exp_list[k-2]
                del exp_list[k-2]
                break
    return int(exp_list[0])

