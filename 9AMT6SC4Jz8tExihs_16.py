
def generate_nonconsecutive(n):
  stack, valids = ["0", "1"], []
  while stack:
    item = stack.pop()
    if len(item) == n:
      valids.append(item)
      continue
    stack.append(item + "0")
    if item[-1] != "1":
      stack.append(item + "1")
  return " ".join(sorted(valids))

