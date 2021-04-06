
def shadow_sentence(a, b):
  a,b = a.split(),b.split()
  return len(a)==len(b) and all([len(a[i])==len(b[i]) for i in range(len(a))]) and all([all([i not in b[j] for i in a[j]]) for j in range(len(a))])

