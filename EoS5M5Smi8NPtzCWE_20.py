
def secret(text):
  
  txt = text.split('*')
  
  item = '<{}></{}>'.format(txt[0], txt[0])
  
  return item * int(txt[1])

