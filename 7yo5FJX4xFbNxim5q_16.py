
def harry(matrix):
  if not matrix[0]:
    return -1
  if len(matrix[0]) == 1:
    return matrix[0][0]
  transpose = tuple(zip(*matrix))
  return max(
    (
      sum(matrix[0]) - matrix[0][-1] + sum(transpose[-1]),
      sum(matrix[-1]) - matrix[-1][0] + sum(transpose[0]),
    )
  )

