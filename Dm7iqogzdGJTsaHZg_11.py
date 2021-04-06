
def retrieve(txt):
  return [i.lower().strip('.') for i in txt.split(' ') \
    if i[0] in 'aeiouAEIOU']  if txt else []

