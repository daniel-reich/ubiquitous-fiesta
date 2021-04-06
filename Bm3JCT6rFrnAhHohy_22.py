
def alphabet_index(txt):
  a = (['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'])
  return ' '.join([str(a.index(i)+1) for i in txt.lower() if i.isalpha()])

