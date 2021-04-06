
def rolling_cipher(txt, n):
  result = ""
  for i in range(len(txt)):
    result += (chr(97+((((ord(txt[i]))+n)-97)%26)))
  return result

