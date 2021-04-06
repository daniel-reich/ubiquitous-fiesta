
def get_languages(num):
  progLngTup=('C#','C++','Java','JavaScript','PHP','Python','Ruby','Swift')
  res=[]
  for i in range(len(progLngTup)):
    bitMask=1<<i
    if num&bitMask: res.append(progLngTup[i])
  return res

