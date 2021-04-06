
faces = {
  ':(': ':)',
  '8(': '8)',
  'x(': 'x)',
  ';(': ';)',
}
​
def make_happy(txt):
  for x in faces:
    if x in txt:
      txt = txt.replace(x, faces[x])
  return txt

