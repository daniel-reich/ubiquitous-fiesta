
import itertools
def simple_equation(*args):
    for a, b, c in itertools.permutations(args):
        for d in '+-*/':
            if eval('{}{}{}=={}'.format(a, d, b, c)):
                return '{}{}{}={}'.format(a, d, b, c)
    return ''

