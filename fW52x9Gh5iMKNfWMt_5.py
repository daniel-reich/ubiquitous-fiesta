
def recaman_index(n):
  seq = [0]
  while seq[-1] != n:
    if seq[-1] - len(seq) > 0 and (seq[-1] - len(seq)) not in seq:
      seq.append(seq[-1]-len(seq))
    else:
      seq.append(seq[-1]+len(seq))
  return len(seq)-1

