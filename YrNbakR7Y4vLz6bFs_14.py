
import itertools
def combinator(lst, sep=''):
    return [sep.join(i) for i in itertools.product(*lst)]

