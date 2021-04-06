
def where_is_waldo(A):
  # Find what the letter is 
  for lst in A:
    if len(set(lst)) != 1:
      for i in set(lst):
        if lst.count(i) == 1:
          letter = i 
  # Find where the letter is 
  for row in A:
    if letter in row:
      row_idx = A.index(row) + 1
  for i in A[row_idx - 1]:
    print(i)
    if i == letter:
      col_idx = A[row_idx - 1].index(i) + 1
​
  return [row_idx, col_idx]

