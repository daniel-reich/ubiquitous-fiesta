
def tap_code(word):
​
  if not(isinstance(word,str)):
    print("You need to input a string")
    return FALSE
  elif "." in word:
    dots = word.split()
    out = []
    for letter in range(0,len(dots),2):
      row = (len(dots[letter])-1+13)*5
      col = len(dots[letter+1])-1
      ascii_val = row+col
      #if ascii_val == 67:
      # out.append("C/K")
      if ascii_val >= 75:
        out.append(str(chr(ascii_val+1)))
      else:
        out.append(str(chr(ascii_val)))
    separator = ''
    out = separator.join(out)
    out = out.lower()
​
  else:
    word = word.upper()
    print(word)
    out = []
    for letter in word:
      ascii_val = ord(letter)
      if ascii_val == 75:
        ascii_val = 67
      elif ascii_val > 75:
        ascii_val -= 1
      row = int(ascii_val/5)-13
      col = ascii_val % 5
      out.append((row+1)*".")
      out.append(" ")
      out.append((col+1)*".")
      out.append(" ")
    out.pop()
    separator = ''
    out = separator.join(out)
  return out

