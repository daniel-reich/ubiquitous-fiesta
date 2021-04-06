
def secret(text):
  x = text.split('*')
  return ''.join('<' + x[0] + '>' if i % 2 == 0 else "</" + x[0] + '>' for i in range(int(x[1])*2))

