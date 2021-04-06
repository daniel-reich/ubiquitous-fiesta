
def find_broken_keys(txt1, txt2): 
  result = []
  for i in range(len(txt1)):
    if txt1[i] != txt2[i]:
      if txt1[i] not in result:
        result += txt1[i]
  return result

