
def closest_palindrome(num):
  def is_pal(num):
    chrs = list(str(num))
    if chrs == chrs[::-1]:
      return True
    return False
  i = num
  j = num
  if is_pal(num):
    return num
  while i>0:
    i -= 1
    j += 1
    if is_pal(i):
      return i
    if is_pal(j):
      return j

