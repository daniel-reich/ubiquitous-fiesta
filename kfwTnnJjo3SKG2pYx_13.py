
def replace_nums(string):
  import re
  string = re.split("(\D)", string)
  for i, j in enumerate(string):
    try:
      string[i] = bin(int(j))[2:]
    except:
      pass
  return "".join(string)

