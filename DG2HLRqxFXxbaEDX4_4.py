
def return_only_integer(lst):
  NumList = []
  for num in lst:
    try: num // 1
    except: continue
    if type(num) == int:
      NumList.append(num)
  return NumList

