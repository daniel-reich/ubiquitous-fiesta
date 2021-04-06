
def remove_special_characters(txt):
  rem = ''
  non = ['!','@','#','$','%','^','&','*','(',')','.','?','/','+','=','[',']','{','}',',','<','>','`','~','|','']
  for x in txt:
     if x not in non:
      rem += x
  return rem

