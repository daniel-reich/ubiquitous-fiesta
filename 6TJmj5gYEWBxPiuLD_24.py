
def seating_students(c):
  col_1 = [i if i not in c[1:] else "#" for i in range(1, c[0]+1, 2)]
  col_2 = [i if i not in c[1:] else "#" for i in range(2, c[0]+1, 2)]
​
  col_1_n = sum([1 if col_1[i] != "#" and col_1[i+1] != "#" else 0 for i in range(len(col_1)-1)])
  col_2_n = sum([1 if col_2[i] != "#" and col_2[i+1] != "#" else 0 for i in range(len(col_2)-1)])
​
  col_1_2_n = sum([1 if col_1[i] != "#" and col_2[i] != "#" else 0 for i in range(min(len(col_1), len(col_2)))])
​
  return sum([col_1_n, col_2_n, col_1_2_n])

