
def transform_matrix(m):
  columns  = transpose(m);
  return [[sum(m[r_idx]) + sum(columns[c_idx]) - 2*m[r_idx][c_idx] for c_idx in range(0 , len(columns)) ] for r_idx in range (0 , len(m)) ];
  
def transpose(mtx):
  columns_count =  len(mtx[0]);
  return [[row[colmn] for row in mtx ] for colmn in range(0 , columns_count)];

