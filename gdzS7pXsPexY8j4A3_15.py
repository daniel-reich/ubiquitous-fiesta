
def count_digits(lst, t):
  def in_number(number, mode):
    odd = sum(1 for i in str(number) if int(i)%2)
    if mode == "odd": return odd
    return len(str(number)) - odd
  return [in_number(i, t) for i in lst]

