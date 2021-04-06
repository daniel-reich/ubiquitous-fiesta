
def valid_word_nest(w,n):
  while n!='':
    if n.count(w)!=1:return 0
    n=n.replace(w,'')
  return 1

