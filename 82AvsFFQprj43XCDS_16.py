
import string
def no_strangers(txt):
  txt = ''.join([i.lower() for i in txt if i not in '.,"']).split()
  d = {}
  aquaintances = []
  friends = []
  for i in txt:
    if i not in d:
      d[i] = 1
    else:
      d[i] += 1
    if d[i] == 3 and d[i] not in aquaintances and d[i] not in friends:
      aquaintances.append(i)
    if d[i] == 5 and d[i] not in friends:
      friends.append(i)
      aquaintances.remove(i)
  return [aquaintances, friends]

