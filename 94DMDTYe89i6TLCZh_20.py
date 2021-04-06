
def get_languages(num):
  lst = []
  langs = iter(('C#', 'C++', 'Java', 'JavaScript', 'PHP', 'Python', 'Ruby', 'Swift'))
  while num > 0:
    lang = next(langs)
    if num & 1:
      lst.append(lang)
    num >>= 1
  return sorted(lst)

