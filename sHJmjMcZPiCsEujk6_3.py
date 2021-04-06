
def pilish_string(txt):
  print(txt)
  pi = "314159265358979"
  arr = []
  prev_i = 0
  for i in pi:
    i = prev_i + int(i)
    if int(i) <= len(txt):
      arr.append(txt[prev_i:int(i)])
      prev_i = int(i)
    else:
      if prev_i < len(txt):
        last_word = txt[prev_i:]
        last_word += last_word[-1] * (int(i) - prev_i - len(last_word))
        arr.append(last_word)
      break
  return " ".join(arr)

