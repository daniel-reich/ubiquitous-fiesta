
def dial(txt):
  convr = [('abc', '2'), ('def', '3'), ('ghi', '4'), ('jkl', '5'), ('mno', '6'), 
('pqrs', '7'), ('tuv', '8'), ('wxyz', '9')]
  pnum = []
  for n in txt.lower():
    if not n.isalpha(): pnum.append(n)
    for t in convr:
      if n in t[0]: pnum.append(t[1])
  return ''.join(pnum)

