
def lambda_to_def(code):
  import re
  from collections import Counter
  after_lambda = code.split("lambda ",1)[1]
  for i, j in enumerate(after_lambda):
    if j == ":" and Counter(after_lambda[:i])["'"]%2 == 0:
      arg_list = after_lambda[:i]
      return_value = after_lambda[i+1:]
  return "def " + code.split(" =")[0] + "(" + arg_list + "):\n\treturn" \
  + return_value

