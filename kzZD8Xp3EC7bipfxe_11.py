
def worded_math(equ):
  numbers = {"zero": "0", "one": "1", "two": "2"}
  op = {"plus": "+", "minus": "-"}
  split = equ.lower().split()
  res = eval(numbers[split[0]] + op[split[1]] + numbers[split[2]])
  return "Two" if res == 2 else "One" if res == 1 else "Zero"

