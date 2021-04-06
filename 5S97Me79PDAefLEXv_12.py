
import re
def lambda_to_def(code):
  func = re.search(r'(\w+)(\s\=\slambda\s)(.+)(\:\s)([^\:]+((?<=\')\:)?.+)',code)
  return "def {}({}):\n\treturn {}".format(func.group(1),func.group(3),func.group(5))

