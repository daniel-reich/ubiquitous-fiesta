
def is_unfair_hurdle(hurdles):
  return all(len(i)<4 for i in hurdles[0].split('#')) or len(hurdles)>3

