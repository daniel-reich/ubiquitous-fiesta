
def sort_by_string(lst, txt):
        
  lst.sort(key = lambda x: txt.index(x[0]))
  return lst

