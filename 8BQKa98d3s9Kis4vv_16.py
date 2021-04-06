
def final(r, c, indices):
  mtx = [];
  incremented_rows = [int(e[0]) for e in indices if e[1] == "r"];
  incremented_cols = [int(e[0]) for e in indices if e[1] == "c"];
  for row_idx in range(0 , r):
    current_row = [];
    for column_idx in range(0,c):
      e = incremented_rows.count(row_idx) + incremented_cols.count(column_idx);
      current_row.append(e);
    mtx.append(current_row);
  return mtx;

