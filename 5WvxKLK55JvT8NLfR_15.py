
def diag_dom(matrix):
  for r, row in enumerate(matrix):
    total = sum(abs(item) for item in row)
    for i, item in enumerate(row):
      if r == i:
        diag = abs(item)
        if not diag > total - diag:
          return False
  return True

