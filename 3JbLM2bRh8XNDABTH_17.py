
def basic_calculator(a, o, b):
  if o == "+":
    return a + b
  if o == "-":
    return a - b
  if o == "/":
    if b == 0:
      return None
    else:
      return a / b
  if o == "*":
    return a * b
​
​
​
print(basic_calculator(4, "+", 3))

