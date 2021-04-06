
def fibonacciSequence():
  seq=[0,1]
  i=1
  while (seq[i] + seq[i - 1])<255:
    seq.append(seq[i]+seq[i-1])
    i += 1
  return seq

