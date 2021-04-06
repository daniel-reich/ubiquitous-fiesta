
def oddish_or_evenish(num):
  new_list = []
  list_nums = list(str(num))
  for number in list_nums:
    new_list.append(int(number))
    
  if (sum(new_list) % 2) == 0:
    return "Evenish"
  else:
    return "Oddish"

