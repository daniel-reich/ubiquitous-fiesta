
def decode(txt):
  len_txt = len(txt)
  lst = []
  for letter in txt:
    num_ord = ord(letter)
    sum = 0
    for num in str(num_ord):
      sum += int(num)
    lst.append(sum) 
  return lst

