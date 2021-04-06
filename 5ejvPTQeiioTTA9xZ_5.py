
def int_or_string(var):
  try:
    catch = int(var)
    return("int")
  except:
    return("str")

