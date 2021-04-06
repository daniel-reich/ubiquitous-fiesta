
def does_rhyme(t1, t2):
  l = "aeiuo"
  v1 = [i for i in t1.lower().split()[-1] if i in l]
  v2 = [i for i in t2.lower().split()[-1] if i in l]
  return v1 == v2

