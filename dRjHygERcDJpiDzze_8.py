
def lengthen(s1, s2):
  short, long = sorted([s1, s2], key=len)
  return (short*10)[:len(long)]

