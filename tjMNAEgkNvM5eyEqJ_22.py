
def unique_abbrev(abbs, words):
  result=[1 for i in range(0,len(words)) for j in range(len(abbs)) if words[i].startswith(abbs[j]) ]
  return sum(result)==len(words)

