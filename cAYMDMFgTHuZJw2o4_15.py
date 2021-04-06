
def reverse_image(image):
  return [[0 if y==1 else 1 for y in x] for x in image]

