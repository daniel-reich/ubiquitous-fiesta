
def ascending(txt):
  for n_len in range(1, (int)(len(txt)/2)+1):
      if len(txt)%n_len != 0:
          continue
      prev = int(txt[:n_len])
      i = n_len
      has_asc = True
      while i+n_len < len(txt)+1:
          curr = int(txt[i:i+n_len])
          if curr - prev != 1:
              has_asc = False
              break
          i += n_len
          prev = curr
      if has_asc:
          return True
  return False

