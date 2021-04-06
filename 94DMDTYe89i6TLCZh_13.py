
def get_languages(num):
  d = ['C#',
  'C++',
  'Java',
  'JavaScript',
  'PHP',
  'Python',
  'Ruby',
  'Swift']
  s = list(bin(num)[2:])
  s.reverse()
  langs = []
  for i in range(len(s)):
    if s[i] == '1':
      langs.append(d[i])
  return langs

