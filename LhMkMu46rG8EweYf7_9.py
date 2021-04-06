
import string
def sort_by_letter(lst):
  return sorted(lst, key = letterof)
  
  
def letterof(elem):
  lowercase = string.ascii_lowercase
  return list([x for x in elem if x in lowercase])[0]

