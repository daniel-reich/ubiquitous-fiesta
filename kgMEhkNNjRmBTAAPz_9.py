
def remove_special_characters(txt):
  for i in set(txt):
    if i.isalnum() == False and i not in '-_ ':
      txt = txt.replace(i,'')
      
  return txt

