
def longest_word(s):
  polje = s.split()
  return max(polje,key=len)

