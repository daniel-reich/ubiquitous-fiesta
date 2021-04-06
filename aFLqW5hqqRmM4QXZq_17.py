
def bar_chart(results):
  s1 = sorted(results.items(), key=lambda x: x[0])
  sRes = sorted(s1, key=lambda x: x[1], reverse=True)
  string = ""
  for item in sRes:
    string += item[0] + "|"
    for i in range(int(item[1]/50)):
      string += "#"
      if i == item[1]/50 - 1:
        string += " "
    string += str(item[1])
    string += "\n"
  return string[:-1]

