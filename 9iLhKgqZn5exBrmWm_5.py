
def ascending(s):
  l = len(s)
  a = list(list(int(s[x * i:x * i + i]) for x in range(l // i))
    for i in range(1, 1 + l // 2) if l % i == 0)
  return any(all(e[i] + 1 == e[i + 1] for i in range(len(e) - 1)) for e in a)

