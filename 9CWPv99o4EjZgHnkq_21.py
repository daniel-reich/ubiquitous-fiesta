
def divide(lst, n):
  final = []
  chunk = []
  for i in range(len(lst)):
    chunk.append(lst[i])
    if i == len(lst) - 1 or sum(chunk + [lst[i + 1]]) > n:
      final.append(chunk)
      chunk = []
  return final

