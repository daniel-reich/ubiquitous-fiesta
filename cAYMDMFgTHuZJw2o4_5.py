
def reverse_image(image):
  return [[y + 1 if y == 0 else y - 1 for y in x] for x in image]

