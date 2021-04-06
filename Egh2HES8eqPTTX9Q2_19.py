
import string
​
def rolling_cipher(txt, n):
  abc = string.ascii_lowercase
  res_str = ""
  for c in txt:
    index  = abc.find(c) + n
    if index > 25:
      index  = index - 26
    res_str += abc[index]
  return res_str

