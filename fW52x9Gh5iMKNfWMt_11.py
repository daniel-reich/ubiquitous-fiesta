
def recaman_index(num):
  seq  = [0];
  while (seq[-1] != num):
    diff  =seq[-1] - len(seq);
    if (diff > 0) and (not diff in seq):
      seq.append(diff);
    else :
      to_add = seq[-1] + len(seq);
      seq.append(to_add);
  return len(seq)-1;

