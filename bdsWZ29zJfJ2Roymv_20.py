
def swap_two(txt):
  lst = [txt[i:i+4] for i in range(0,len(txt),4)]
  return ''.join(i[2:]+i[:2] if len(i)==4 else i for i in lst)

