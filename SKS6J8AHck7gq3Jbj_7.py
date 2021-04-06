
def tidy_books(lst):
  l1 = []
  l2 = []
  for i in lst:
    for x in i:
      new_txt = [y.strip() for y in str(x).split("-")]
      l1.append(new_txt)
  return l1
  
# return [[",".join("".join(x.split()))] for i in lst for x in str(i).split('-')]

