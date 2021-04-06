
pi = 3.14159265358979
def pilish_string(txt):
  phrase = ""
  pi_str = str(pi).replace(".", "")
  for max_len in pi_str:
    if not txt:
      break
    word = txt[:int(max_len)]
    if len(word) > int(max_len):
      break
    
    while len(word) != int(max_len):
      word += word[-1]
    phrase += " " + word
    txt = txt[int(max_len):]
    
  return phrase[1:]

