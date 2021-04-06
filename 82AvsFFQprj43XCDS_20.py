
def no_strangers(txt):
  import re
  txt=txt.lower()
  txt=re.sub('[^a-zA-Z0-9 \n\']', '', txt)
  txt=txt.split()
  test={}
  accq = []
  friend = []
  for i in txt:
    test[i] = 1 if i not in test else test[i] + 1
    if test[i] == 3: accq.append(i)
    if test[i] == 5:
      friend.append(i)
      accq.remove(i)
  return [accq,friend]

