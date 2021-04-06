
def seating_students(lst):
  import itertools 
  no,*occupied=lst
  cr=[[i if i not in occupied else '#' for i in range(2,no+1,2)],[i if i not in occupied else '#' for i in range(1,no,2)]]
  row_groups1=[(cr[0][i],cr[0][i+1]) for i in range(len(cr[0])-1) if cr[0][i]!='#' and cr[0][i+1]!='#']
  row_groups2=[(cr[1][i],cr[1][i+1]) for i in range(len(cr[1])-1) if cr[1][i]!='#' and cr[1][i+1]!='#']
  col_groups=[(i,j) for i,j in list(zip(cr[0],cr[1])) if i!='#' and j!='#']
  col_groups.extend(row_groups1)
  col_groups.extend(row_groups2)
  return len(col_groups)

