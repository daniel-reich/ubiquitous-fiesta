
def multiply_matrix(m1, m2):
  C = []
  idx, len_m1, len_m2 = 0, len(m1[0]), len(m2[0])
​
  if len_m1 != len(m2):
    return "ERROR"
​
  while idx != len(m1):
    res_arr = [0 for _ in range(len_m2)]
    for i in range(len_m1):
      for j in range(len_m2):
        res_arr[j] += m1[idx][i] * m2[i][j]
    C.append(res_arr)
    idx += 1
  return C

