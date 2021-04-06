
def chunkify(li, n):
  return [li[i:i+n] for i in range(0, len(li), n)]

