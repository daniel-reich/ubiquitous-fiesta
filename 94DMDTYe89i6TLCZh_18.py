
def get_languages(num):
  langs = ['C#','C++','Java','JavaScript','PHP','Python','Ruby','Swift']
  num = bin(num)[2:][::-1]
  return [langs[i] for i in range(len(num)) if int(num[i])]

