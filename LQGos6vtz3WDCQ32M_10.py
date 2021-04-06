
def Kaprekar(n):
    str_n = str(n)
    first_line = '\n---------- The Mysterious Number 6174 ----------\n'
    last_line = '\n------------------------------------------------'
    if len(str_n) > 1 and len(set(str_n)) == 1:
        middle_line = '\nError, n cannot be a repdigit.\n'
    else:
        lst_triple = []
        while n != 6174:
            lst_n = list('{:0>4}'.format(str(n)))
            large_n = int(''.join(sorted(lst_n, reverse=True)))
            small_n = int(''.join(sorted(lst_n)))
            n = large_n - small_n
            lst_triple.append((large_n, '{:0>4}'.format(str(small_n)),
                               '{:0>4}'.format(str(n))))
        middle_line = '\nNumber of iterations: {}\n'.format(len(lst_triple))
        middle_line += '\nIterations:\n\n'
        for idx, tpl in enumerate(lst_triple):
            middle_line += 'Iteration Nr. {}: {} - {} = {}\n'.format(idx + 1,
                                                                     *tpl)
    return first_line + middle_line + last_line

