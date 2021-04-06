
import re
def lambda_to_def(code):
  A=re.split('\s=\slambda\s|:\s', code)
  return "def {0}({1}):\n\treturn {2}".format(A[0], A[1], A[2])

