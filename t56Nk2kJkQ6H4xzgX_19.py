
import ast
​
def swap_xy(txt):
  lt = list(ast.literal_eval(txt))
  for i in range(0, len(lt)):
    lt[i] = tuple(reversed(lt[i]))
  return str(lt).strip('[]')

