
def coloured_triangle(row):
   d = {'BG':'R', 'BR': 'G', 'GR': 'B',
     'BB':'B', 'GG':'G', 'RR':'R'}
   while len(row) > 1:
      nxt =''
      for i in range(len(row)-1):
         k = ''.join(sorted([x for x in row[i:i+2]]))
         nxt += d[k]
      row = nxt
   return row

