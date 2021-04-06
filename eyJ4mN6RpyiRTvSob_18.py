
def is_palindrome_possible(txt):
  lst = sorted(txt,key=txt.count)
  if lst.count(lst[0]) == 1:
    del lst[0]
  return all(not lst.count(ch)%2 for ch in lst)

