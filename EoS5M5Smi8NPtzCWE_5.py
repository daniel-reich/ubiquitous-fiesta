
def secret(text):
  txt = text.split('*')[0]
  num = text.split('*')[1]
  return '<{}></{}>'.format(txt, txt) * int(num)

