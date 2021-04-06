
def true_equations(lst):
  return [i for i in lst if tryEquate(i)]
​
def tryEquate(s):
  a,b = s.split("=")
  return eval(a)==int(b)

