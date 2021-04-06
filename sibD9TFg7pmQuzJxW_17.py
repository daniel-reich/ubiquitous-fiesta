
def stem_plot(lst):
  ans = []
  s = set()
  for i in sorted(lst):
    if i < 10 and '0' in s:
      v = [x for x in range(len(ans)) if ans[x].split(' | ')[0] == '0'][0]
      ans[v] = ans[v] + ' ' + str(i)
    elif i >= 10 and str(i)[0:-1] in s:
      v = [x for x in range(len(ans)) if ans[x].split(' | ')[0] == str(i)[0:-1]][0]
      ans[v] = ans[v] + ' ' + str(i)[-1:]
    elif i < 10 and '0' not in s:
      ans.append("0 | " + str(i))
      s.add('0')
    elif i >= 10 and str(i)[0:-1] not in s:
      ans.append(str(i)[0:-1] + " | " + str(i)[-1:])
      s.add(str(i)[0:-1])
  return ans

