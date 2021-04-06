
def digit_sort(lst):
  tenthou, thou, hun, ten, digi = [],[],[],[],[]
  for i in lst:
    if i < 10: digi.append(i)
    elif i < 100: ten.append(i)
    elif i < 1000: hun.append(i)
    elif i < 10000: thou.append(i)
    else: tenthou.append(i)
  return sorted(tenthou) + sorted(thou) + sorted(hun) + sorted(ten) + sorted(digi)

