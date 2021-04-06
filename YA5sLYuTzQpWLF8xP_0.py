
def clean_up_list(lst):
  odd = []
  even = []
  for i in lst:
    if int(i)%2 == 0:
      even.append(int(i))
    else:
      odd.append(int(i))
  return [even, odd]

