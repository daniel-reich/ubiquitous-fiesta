
def last_name_lensort(names):
  names_list = []
  for n in names:
    names_list.append(n.split(" "))
  names_sorted = sorted(names_list, key=lambda x:x[1])
  names_sorted = sorted(names_sorted, key=lambda x:len(x[1]))
  names_final = []
  for j in range(0, len(names_sorted)):
    names_final.append(" ".join(names_sorted[j]))
  return names_final

