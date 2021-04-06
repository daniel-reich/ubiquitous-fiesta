
def secret(text):
  text = text.split('*')
  return ''.join(['<' + text[0] + '></' + text[0] + '>' for i in range(int(text[1]))])

