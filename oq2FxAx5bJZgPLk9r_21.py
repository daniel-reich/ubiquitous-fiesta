
def sock_merchant(lst):
  unique_colors = set(lst)
  return sum(lst.count(color) // 2 for color in unique_colors)

