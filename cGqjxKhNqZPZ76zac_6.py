
def fire(matrix, c):
  return ['BOOM', 'splash'][matrix[ord(c[0])-65][int(c[1])-1]=='.']

