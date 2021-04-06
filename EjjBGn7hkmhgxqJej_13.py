
def word_nest(word, nest):
  count = 0
  while True:
    nest = nest.replace(word,'')
    count+=1
    if len(nest)==0:
      break
  return count-1

