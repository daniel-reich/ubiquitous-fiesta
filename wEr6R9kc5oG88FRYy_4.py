
def get_frame(w, h, ch):
  if w <= 2 or h <= 2:
    return "invalid"
  width = [ch*w]
  product = []
  product.append(width)
  for i in range(h-2):
    product.append([ch + " "*(w-2) + ch])
  product.append(width)
  return product

