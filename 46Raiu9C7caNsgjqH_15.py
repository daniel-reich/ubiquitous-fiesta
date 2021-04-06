
def compare_data(*args):
  print(args)
  t = True
  for i in range(len(args)):
    if isinstance(args[i], type(args[0])):
      pass
    else:
      t = False
      print("boop")
      break
  return t

