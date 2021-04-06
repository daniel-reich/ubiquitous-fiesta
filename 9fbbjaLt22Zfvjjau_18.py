
uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def paul_cipher(txt):
  result, char = '', False
  for i in txt.upper():
    if i in uppercase and not char:
      result += i
      char = i
    elif i in uppercase:
      if uppercase.find(char)+uppercase.find(i)+1 >= len(uppercase):
        result += uppercase[uppercase.find(char)+uppercase.find(i)+1-26]
        char = i
      else:
        result += uppercase[uppercase.find(char)+uppercase.find(i)+1]
        char = i
    else:result += i
  return result

