
def split_code(item):
  pos=0
  while pos<len(item):
    if item[pos].isdigit(): break
    pos+=1
  return [item[0:pos], int(item[pos:])]

