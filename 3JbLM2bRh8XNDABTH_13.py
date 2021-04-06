
def basic_calculator(a, o, b):
  try:
    return eval(str(a) + o + str(b))
  except:
    return None

