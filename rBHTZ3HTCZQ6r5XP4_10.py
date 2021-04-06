
def expanded_form(num):
    whole, decimal = str(num).split('.')
    first = [i + '0'*idx for idx, i in enumerate(whole[::-1]) if i != '0'][::-1]
    second = [i + '/' + str(10**idx) for idx, i in enumerate(decimal, 1) if i != '0']
    return ' + '.join(first + second)

