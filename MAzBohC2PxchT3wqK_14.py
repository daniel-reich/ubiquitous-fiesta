
def shadow_sentence(a: str, b: str) -> bool:
  a = a.split(); b = b.split()
  if [len(word) for word in a] != [len(word) for word in b]:
    return False
  return all(set(a[i]).isdisjoint(set(b[i])) for i in range(len(a)))

