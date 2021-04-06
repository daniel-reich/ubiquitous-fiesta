
def is_repdigit(num):
  result = []
  if num < 0: return False
  for i in range(len(str(num))):
    if str(num)[i] == str(num)[0]:
      result.append(True)
    else:
      result.append(False)
  if all(result): return True
  else: return False

