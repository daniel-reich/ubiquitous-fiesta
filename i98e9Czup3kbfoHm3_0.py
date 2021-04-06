
def text_to_number_binary(txt):
  s = ''.join('1' if t.lower()=='one' else '0' if t.lower()=='zero' else '' for t in txt.split(' '))
  return s[:(8*(len(s)//8))]

