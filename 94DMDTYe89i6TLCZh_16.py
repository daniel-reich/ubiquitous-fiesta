
def get_languages(num):
  lang = ['Swift','Ruby','Python','PHP','JavaScript','Java','C++','C#']
  b = list(bin(num))
  codes = ['0']*(10-len(b))+b[2:]
  return sorted([lang[i] for i in range(8) if codes[i]=='1'])

