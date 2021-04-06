
def minesweeper_numbers(lst):
  A=[[0 for j in range(len(lst[0]))] for i in range(len(lst))]
  for i in range(len(lst)):
    for j in range(len(lst[0])):
      if lst[i][j]==1:
        A[i][j]=9
      else:
        A[i][j]=[lst[k][t] for k in range(len(lst)) for t in range(len(lst[0])) if abs(i-k)<2 and abs(j-t)<2].count(1)
  return A

