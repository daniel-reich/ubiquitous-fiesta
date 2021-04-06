
def get_languages(score):
  d = { 
  'C#': 1,
  'C++':  2,
  'Java': 4,
  'JavaScript': 8,
  'PHP':  16,
  'Python': 32,
  'Ruby': 64,
  'Swift':  128
  }
  d = {v : k for k, v in d.items()}
  l = [] 
  i = 1
  while i < 128 or i == 128:
    l.append(i)
    i *= 2
  l.sort(reverse = True)
  langs = [] 
  while score != 0:
    for i in l:
      if i == score or i < score:
        langs.append(d[i])
        score -= i
  langs.sort()
  return langs

