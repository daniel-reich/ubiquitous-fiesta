
def word_nest(word, nest):
  c=0
  while nest:
    nest=nest.replace(word,'')
    c+=1
  return c-1

