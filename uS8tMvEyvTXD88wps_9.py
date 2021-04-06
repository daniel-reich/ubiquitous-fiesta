
def reverse(txt):
  lst = txt.split(" ")
  lst2 = []
  for i in range(0, len(lst)):
    if len(lst[i]) > 4 and i != len(lst)-1:
      lst2.append(lst[i][::-1] + " ")
    elif len(lst[i]) > 4 and i == len(lst)-1:
      lst2.append(lst[i][::-1])
    elif i == len(lst)-1:
      lst2.append(lst[i])
    else:
      lst2.append(lst[i] + " ")
  return "".join(lst2)

