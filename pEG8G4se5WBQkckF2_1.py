
def reverse_sort(txt):
  lst = txt.split(" ")
  lst = sorted(lst, key= lambda x: x.lower(), reverse= True)
  lst = sorted(lst, key= lambda x: len(x), reverse= True)
  return " ".join(lst)

