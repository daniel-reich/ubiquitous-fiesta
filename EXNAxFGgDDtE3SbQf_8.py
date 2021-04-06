
def shuffle_count(num):
  numlst=[i for i in range(num)]
  numlst1,numlst2=numlst[:int(num/2)],numlst[int(num/2):]
  numlstshuffled=[]
  while numlst1 and numlst2:
    numlstshuffled.append(numlst1.pop(0))
    numlstshuffled.append(numlst2.pop(0))
  def shuffle(numlstshuffled):
    if numlstshuffled==numlst:
      return 1
    else:
      numlst1,numlst2=numlstshuffled[:int(num/2)],numlstshuffled[int(num/2):]
      numlstshuffled=[]
      while numlst1 and numlst2:
        numlstshuffled.append(numlst1.pop(0))
        numlstshuffled.append(numlst2.pop(0))
    return 1+shuffle(numlstshuffled)
  return shuffle(numlstshuffled)

