
def syllabification(word):
​
  vowels = 'a, A, e, i, o, u'.split(', ')
  vowel_indexes = []
​
  for n in range(len(word)):
    l8r = word[n]
    if l8r in vowels:
      vowel_indexes.append(n)
  
  if len(vowel_indexes) == 0:
    return word
​
  section_beginnings = {}
​
  for index in vowel_indexes:
    section_beginnings[index] = index - 1
  
  section_endings = {}
​
  for n in range(len(vowel_indexes) - 1):
    index = vowel_indexes[n]
    backstop = section_beginnings[vowel_indexes[n+1]]
​
    section_endings[index] = backstop
​
  sections = []
​
  for index in vowel_indexes:
    
    start = section_beginnings[index]
    try: 
      end = section_endings[index]
    except KeyError:
      end = None
    
    if end == None:
      sections.append(word[start:])
    else:
      sections.append(word[start:end])
  
  return '.'.join(sections)

