
def sort_by_last(txt):
  a = txt.split(' ')
  final_list = []
  for i in range(len(a)):
    last_char = a[i][-1]
    final_list.append([i, last_char, a[i]])
  final_list.sort(key=lambda x: x[1])
  items = [el[2] for el in final_list]
  return ' '.join(items)

