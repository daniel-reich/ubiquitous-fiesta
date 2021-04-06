
def reverse_image(image):
  for x in image:
    for i in range(len(x)):
      x[i]=1-x[i]
  return image

