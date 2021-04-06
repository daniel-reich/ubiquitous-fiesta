
def palindrome_time(lst):
  im = sum([1 for i in range(lst[0], lst[3]) if i < 6 or (i > 9 and i < 16) or i > 19 ])
  im -= 1
  mt1 = 0
  mt2 = 0
  if im >= 0:
    for it in range(0, 56, 11):
      if it >= lst[1]: mt1 += 1
      if it <= lst[4]: mt2 += 1
  elif im == -1:
    im = 0
    for it in range(lst[1], lst[3], 1):
        if it >= lst[1] and it % 11 == 0: mt1 += 1
  return im*6 + mt1 + mt2

