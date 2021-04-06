
def recaman_index(n):
  seq, i = [0], 1
  while True:
    if seq[-1] - i > 0 and seq[-1] - i not in seq: seq+= [seq[-1] - i]
    else: seq+= [seq[-1] + i]
    if seq[-1] == n: return i
    i+=1

