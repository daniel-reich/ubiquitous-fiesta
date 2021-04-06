
def worm_length(worm):
  return (str(len(worm) * 10) + " mm.") if set([i for i in worm]) == {"-"} else "invalid"

