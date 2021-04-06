
def get_languages(num):
  lang = ['Swift', 'Ruby', 'Python', 'PHP', 'JavaScript', 'Java', 'C++', 'C#']
  return sorted([x for x,y in zip(lang,list('{0:08b}'.format(num))) if y is '1'])

