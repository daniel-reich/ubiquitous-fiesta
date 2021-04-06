
def all_about_strings(txt):
  one = len(txt)
  d = int(len(txt)/2) if not len(txt) % 2 else int(len(txt)//2)
  two = txt[0]
  three = txt[-1]
  four = txt[(d-1):(d+1)] if not len(txt) % 2 else txt[len(txt)//2]
  five = "".join(["@ index " + str(i)  for i,v in enumerate(txt) if v == txt[1] and i != 1 ]) if txt.count(txt[1]) > 1 else "not found"
  return [one,two,three,four,five]

