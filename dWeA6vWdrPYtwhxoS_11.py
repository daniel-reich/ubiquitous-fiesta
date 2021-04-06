
import string
def count_number(lst):
  digits = string.digits
  count = 0
  lst = ((str(lst).replace('[','')).replace(']','')).split(' ')
  for eachvalue in lst:
    for eachletter in eachvalue:
      if eachletter in digits or eachletter == '.':
        count += 1
        break
      else:
        continue
  return count

