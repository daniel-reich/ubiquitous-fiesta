
import re
def find_shortest_words(txt):
  txt = re.sub('[^A-Za-z ]+', '', txt).lower().replace("  ", " ").split(" ")
  d = {}
  for i in txt:
      if i not in d:
          d[i] = {"len": len(i), "count": 1}
      else:
          d[i]["count"] += 1
  l = []
  for k, v in d.items():
      if not l:
          for i in range(v["count"]):
              l.append(k)
      else:
          if len(l[0]) == len(k):
              for i in range(v["count"]):
                  l.append(k)
          elif len(k) < len(l[0]):
              l = []
              for i in range(v["count"]):
                  l.append(k)
  return sorted(l)

