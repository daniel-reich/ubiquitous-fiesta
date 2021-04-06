
def factory(n):
  def transpose_list(alist):
    return [x / n for x in alist]
  return transpose_list

