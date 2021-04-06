
def get_languages(num):
  lg = {
    1  :    'C#',
    2  :    'C++',
    4  :    'Java',
    8  :    'JavaScript',
    16 :    'PHP',
    32 :    'Python',
    64 :    'Ruby',
    128:    'Swift'
  }
  s = bin(num)[2:][::-1]
  l_out = []
  for i in range(len(s)):
    if s[i] == '1':
      l_out.append(lg[2**i])
  return l_out

