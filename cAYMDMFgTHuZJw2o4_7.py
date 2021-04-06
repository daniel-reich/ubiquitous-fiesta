
def reverse_image(image):
  output = []
  for i in range(len(image)):
    output.append([])
    for j in range(len(image[i])):
      if image[i][j] == 0:
        output[i].append(1)
      else:
        output[i].append(0)
  return output

