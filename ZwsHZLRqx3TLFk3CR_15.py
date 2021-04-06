
def eval_factorial(lst):
  def fact(f):
   if f == 0:
    return 1
   else :
    return f*fact(f-1)
  lst1 = [int(x.strip("!")) for x in lst]
  return sum([fact(x) for x in lst1])

