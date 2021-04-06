
def evaluate_polynomial(poly, num):
    lst = list(poly)
    for i in range(len(lst)):
        if lst[i] == 'x':
            if i > 0 and lst[i - 1].isdigit():
                lst[i] = '*' + str(num)
            else:
                lst[i] = str(num)
        elif lst[i] == '(':
            if i > 0 and (lst[i - 1].isdigit() or lst[i - 1] == 'x'):
                lst[i] = '*('
        elif lst[i] == '^':
            lst[i] = '**'
        elif lst[i] == '/':
            if i > 0 and lst[i - 1] == '/':
                return 'invalid'
        elif lst[i].isalpha():
            return 'invalid'
    try:
        return int(eval(''.join(lst)))
    except (SyntaxError, TypeError):
        return 'invalid'

