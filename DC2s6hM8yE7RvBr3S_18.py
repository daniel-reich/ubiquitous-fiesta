
def subtract_matrix(lst1, lst2):
  return [
    [
      (
        (int(col_a) if not isinstance(col_a, (int, float)) else col_a)
        - (int(col_b) if not isinstance(col_b, (int, float)) else col_b)
      )
      for col_a, col_b in zip(row_a, row_b)
    ]
    for row_a, row_b in zip(lst1, lst2)
  ]

