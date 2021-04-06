
def get_languages(num):
  return [a for a,b in zip(['C#','C++','Java','JavaScript','PHP','Python','Ruby','Swift'][::-1],[x=='1' for x in '{:0>8}'.format('{:b}'.format(num))]) if b][::-1]

