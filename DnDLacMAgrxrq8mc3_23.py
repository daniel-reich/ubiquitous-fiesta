
def blah_blah(txt, n):
  if len(txt.split())>n:
    return ' '.join(x for x in txt.split()[:-n])+" "+' '.join("blah" for i in range(n))+"..." 
  return " ".join("blah" for s in range(len(txt.split())))+"..."

