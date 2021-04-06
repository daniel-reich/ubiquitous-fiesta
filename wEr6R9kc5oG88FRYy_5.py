
def get_frame(w, h, ch):
  if w <= 2 or h <= 2:
    return "invalid"
  W = ["".join([ch for i in range(w)])]
  H = ["{}{}{}".format(ch," "*(w-2),ch)]
  L = [W]
  for i in range(h-2):
    L.append(H)
  return L+[W]

