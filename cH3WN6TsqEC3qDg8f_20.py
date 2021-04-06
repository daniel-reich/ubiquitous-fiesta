
def rectangle_in_circle(w, h, radius):
  dist_to_corner = ((w/2)**2 + (h/2)**2)**0.5
  return dist_to_corner <= radius

