
def delete_occurrences(lst, num):
  for item in lst: 
    while lst.count(item) > num: 
        lst.reverse()
        lst.remove(item)
        lst.reverse()
  return lst

