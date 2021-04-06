
def order_people(lst, people):
  row_num, col_num = lst
  if row_num * col_num < people:
    return "overcrowded"
  out = []
  start_num = 0
  for row in range(row_num):
    for col in range(col_num):
      sublist = [i + start_num 
          if i + start_num <= people else 0
          for i in range(1, col_num + 1)]
    out.append(sublist)
    start_num += col_num
  for i, l in enumerate(out):
    if i % 2 != 0:  # odd
      out[i] = list(reversed(out[i]))
  return out

