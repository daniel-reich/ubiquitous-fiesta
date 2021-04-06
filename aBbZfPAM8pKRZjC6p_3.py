
def fruit_salad(fruits):
  chunks = []
  for f in fruits:
    chunks.append(f[:len(f)//2])
    chunks.append(f[len(f)//2:])
  return ''.join(sorted(chunks))

