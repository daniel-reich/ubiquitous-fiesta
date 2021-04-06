
def rotate_matrix(mat, turns=1):
  tam=mat[::-1]
  if turns%4==0:
    return mat
  elif turns%4==1:
    return [list(x)[::-1] for x in zip(*mat)]
  elif turns%4==2:
    return [x[::-1] for x in mat][::-1]
  else:
    return [list(x)[::-1] for x in zip(*tam)][::-1]

