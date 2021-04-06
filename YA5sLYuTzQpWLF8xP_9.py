
def clean_up_list(lst):
  even_list = []
  odd_list = []
  for i in lst:
    i = int(i)
    if i%2==0:
      even_list.append(i)
    else:
      odd_list.append(i)
  return [even_list, odd_list ]

