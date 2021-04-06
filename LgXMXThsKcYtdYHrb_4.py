
def split_and_delimit(txt, num, delimiter):
  newTxt = ''
  for i in range(0, len(txt), num):
    newTxt += txt[i:i+num]
    newTxt += delimiter
  return newTxt[:-1]

