
def worded_math(equ):
  d_int_str = {
    0 : "Zero",
    1 : "One",
    2 : "Two",
  }
  d_str_int = {
    "zero" : 0,
    "one" : 1,
    "two" : 2,
  }
  a, sign, b = equ.lower().split(' ')
  a = d_str_int[a]
  b = d_str_int[b]
  return d_int_str[a + b if sign == "plus" else a - b]

