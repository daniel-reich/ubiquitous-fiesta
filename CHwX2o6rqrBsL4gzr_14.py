
def check_title(txt):
  txt = txt.split(" ")
  for i in range(len(txt)):
    if txt[i][0].islower():
      return False;
  return True;

