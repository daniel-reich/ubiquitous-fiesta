
def move_zeros(lst):
  return sorted(
    (0 if i == 0 and type(i) is float else i for i in lst),
    key=lambda x: x is 0
  )

