
def split_and_delimit(txt, num, delimiter):
  mystr = ""
  for i in range (0,len(txt),num):
    mystr += txt[i:i+num] + delimiter 
  return mystr.strip(delimiter)

