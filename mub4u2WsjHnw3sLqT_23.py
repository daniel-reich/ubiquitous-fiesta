
def lambda_depth(num):
  def f():
    nonlocal num
    if num:
      num -= 1
      return f
    else:
      return 'edabit'
  return f()

