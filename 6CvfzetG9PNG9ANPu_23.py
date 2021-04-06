
def mubashir_cipher(message):
  key = [["m", "c"], ["u", "e"], ["b", "g"], ["a", "k"], ["s", "v"], ["h", "x"], ["i", "z"], ["r", "y"], ["p", "w"], ["l", "n"], ["o", "j"], ["t", "f"], ["q", "d"]]
​
  k1, k2 = zip(*key)
​
  return "".join(k2[k1.index(c)] if c in k1 else k1[k2.index(c)] if c in k2 else c for c in message)

