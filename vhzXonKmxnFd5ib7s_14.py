
def matrix_multiply(a, b):
  rows , columns  = a, transpose(b);
  print(rows)
  print(columns)
  if (len(rows[0]) != len(columns[0])):
    return "invalid";
  return [[dot_prod(row , column) for column in columns] for row in rows ];
  
def dot_prod(row , other):
  return sum([a*b for a,b in zip(row , other)]);
  
def transpose(mtx):
  return [[row[colmn] for row in mtx ] for colmn in range(0,len(mtx[0])) ]

