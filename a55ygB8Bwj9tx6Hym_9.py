
import string
def steps_to_convert(txt):
  count = 0
  for i in txt:
    if i in string.ascii_lowercase:
      count +=1
  return min (count, len(txt) - count)

