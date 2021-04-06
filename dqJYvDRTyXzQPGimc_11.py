
def is_unfair_hurdle(hurdles):
  return len(hurdles)>=4 or int(hurdles[0].count(" ")/(hurdles[0].count("#")-1))<4

