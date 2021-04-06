
import itertools
def ping_pong(lst, win):
  if win:
    return list(itertools.chain(*[list(x) for x in zip(lst, ["Pong!"] * len(lst))]))
  else:
    return list(itertools.chain(*[list(x) for x in zip(lst, ["Pong!"] * len(lst))]))[:-1]

