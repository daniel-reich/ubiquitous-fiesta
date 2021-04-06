
def get_languages(num):
  langs ={1:'C#',
    2:'C++',
    4:'Java',
    8:'JavaScript',
    16:'PHP',
    32:'Python',
    64:'Ruby',
    128:'Swift'}
  
  languages = []
  for x in range(8):
    if num&(2**x):
      languages.append(langs[2**x])
  return languages

