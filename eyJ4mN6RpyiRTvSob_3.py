
def is_palindrome_possible(txt):
  return len([i for i in txt if txt.count(i) % 2 == 0]) == len(txt)//2*2

