
#Horrendously inefficient solution
import itertools
​
def countdown(operands, target):
  for perm in itertools.permutations(operands):
    n = len(perm)
    for combo in itertools.product("+-*/", repeat=n-1):
      l = list(combo)
      out = ""
      for i in range(n):
        if i < n-1:
          li = l[i]
          if l[i] == "/":
            li = "//"
          out += str(perm[i]) + li
        else:
          out += str(perm[i])
      if eval(out) == target:
        return out

