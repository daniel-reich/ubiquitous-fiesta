
def next_letters(s):
  temp = list(s)
  temp2 = []
  output = ""
  count = 1
  carry = 1
  for c in temp[::-1]:
    carry = 0
    if(c == 'Z'):
      if(count == 1):
        temp2.insert(0,'A')
        carry = 1
      else:
        temp2.insert(0,c)
        count = 0
    else:
      if(count == 1):
        temp2.insert(0,chr(ord(c)+1))
        count = 0
      else:
        temp2.insert(0,c)
        count = 0
  if carry: temp2.insert(0, 'A')
  for t in temp2:
    output += t
  return output

