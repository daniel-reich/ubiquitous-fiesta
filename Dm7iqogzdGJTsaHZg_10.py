
def retrieve(txt):
  new_lst = []
  for i in txt.split():
    if i[0].lower() in 'aeiou':
      new_lst.append(i.lower().strip('.'))
  return new_lst

