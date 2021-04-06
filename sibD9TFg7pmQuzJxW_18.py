
def stem_plot(lst):
  mp = {}
  stems = []
  for i in lst:
    if int(i / 10) not in mp.keys():
      mp[int(i / 10)] = [i % 10]
      stems.append(int(i / 10))
    else:
      mp[int(i / 10)].append(i % 10)
      mp[int(i / 10)].sort()
  stems.sort()
  final = []
  for i in stems:
    string = str(i) + ' |'
    for j in mp[i]:
      string += ' ' + str(j)
    final.append(string)
  return final

