
def get_languages(num):
  d,r={1:"C#",2:"C++",4:"Java",8:"JavaScript",16:"PHP",32:"Python",64:"Ruby",128:"Swift"},[]
  while num!=0:
    r.append(max(list(filter(lambda x:x<=num,d.keys()))))
    num%=r[-1]
  return [d[i] for i in sorted(r)]

