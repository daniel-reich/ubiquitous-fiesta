
from string import ascii_lowercase as al
def modify(txt):
  txt = txt[::-1]
  num = []
  for letter in txt:
    num.append(str(al.find(letter)+1))
  num = "".join(num)
  num = bin(int(num))[2:]
  return int(num)

