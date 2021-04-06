
def find_zip(txt):
  lst=[i for i in range(len(txt)) if txt[i:i+3]=="zip"]
  return lst[1] if len(lst)>=2 else -1

