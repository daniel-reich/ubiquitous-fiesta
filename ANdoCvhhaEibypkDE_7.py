
def closing_in_sum(n):
  def get_ints(n):
    s = str(n)
    print(s, s[1:-1])
    if len(s) > 2:
      return [s[0] + s[-1]] + get_ints(s[1:-1])
    else:
      return [s]
  
  gi = get_ints(n)
  
  return sum([int(i) for i in gi])

