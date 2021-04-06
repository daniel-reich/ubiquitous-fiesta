
def digits_sum(x):
  return sum(int(i) for i in str(x))
​
def mubashir_function(a, b):
  return digits_sum(a) * digits_sum(b)

