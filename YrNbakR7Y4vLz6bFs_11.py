
import itertools
def combinator(lst,sep=''):
  return [sep.join(p) for p in itertools.product(*lst)]

