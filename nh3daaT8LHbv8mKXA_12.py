
def text_to_num(phone):
  dicts = {'ABC':'2','DEF':'3','GHI':'4','JKL':'5','MNO':'6','PQRS':'7','TUV':'8','WXYZ':'9'}
  out = ""
  for i in phone:
    if i.isalpha():
      for j in dicts.keys():
        if i in j:
          out += dicts[j]
          break
        else:
          continue
    else:
      out += i
  return out

