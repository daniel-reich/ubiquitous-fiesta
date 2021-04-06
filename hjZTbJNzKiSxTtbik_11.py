
def sort_by_string(lst, txt):
  result = []
  for i in range(len(txt)):
    for j in range(len(lst)):
      if txt[i] == lst[j][0]:
        result.append(lst[j])
  return result

