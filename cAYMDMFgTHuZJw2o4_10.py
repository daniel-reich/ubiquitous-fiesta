
def reverse_image(m):
  return [[1 if i[j]==0else 0 for j in range(len(m[0]))] for i in m]

