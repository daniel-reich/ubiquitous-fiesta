
def max_separator(txt):
  lst = []
  for idx, letter in enumerate(txt):
    if txt[idx:].count(letter) >= 2:
      lst.append([txt[idx+1:].index(letter) - txt[idx].index(letter), letter])
  return sorted([i[1] for i in lst if i[0] == max(lst)[0]])

