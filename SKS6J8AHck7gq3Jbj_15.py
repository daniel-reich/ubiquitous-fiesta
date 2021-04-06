
def tidy_books(lst):
  
  clean = []
  
  for val in lst:
    title, author = (val[0].split(' - '))
    clean.append([title.strip(), author.strip()])
    
  return clean

