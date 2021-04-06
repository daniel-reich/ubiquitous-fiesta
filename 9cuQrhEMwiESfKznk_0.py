
def eng2nums(s):
  lst1 = ['zero','one','two','three','four','five','six','seven',
  'eight','nine','ten','eleven','twelve','thirteen','fourteen',
  'fifteen','sixteen','seventeen','eighteen','nineteen','twenty','thirty',
  'forty','fifty','sixty','seventy','eighty','ninety','hundred']
  lst2 = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,
  30,40,50,60,70,80,90,100]
  d = dict([[lst1[i],lst2[i]] for i in range(len(lst1))])
  if ' ' in s:
    s = s.split()
  else:
    s = [s]
  ret = 0
  if 'hundred' in s:
      ret+=d[s[0]]*d[s[1]]
      ret+=sum([d[i] for i in s[2:]])
  else:
    ret+=sum([d[i] for i in s])
  return ret

