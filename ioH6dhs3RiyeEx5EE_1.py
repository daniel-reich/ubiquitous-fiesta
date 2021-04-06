
def make_fun_lst(n1, n2):
    return [eval('lambda x: x * k', {'k': i}) if i % 2 else
            eval('lambda x: x + k', {'k': i}) for i in range(n1, n2)]

