
def look_and_say(start, n):
  s = str(start)
  res = [start]
  for _ in range(n - 1):
    d = [ [s[0], 1] ]
    for c in s[1:]:
      if d[-1][0] == c:
        d[-1][1] += 1
      else:
        d.append([c, 1])
    s = "".join(str(v)+k for k,v in d)
    res.append(int(s))
  return res

