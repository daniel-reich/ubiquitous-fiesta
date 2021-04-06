
def split_code(x):
  letters = "".join([i for i in x if i.isalpha()])
  nums = "".join([i for i in x if i.isnumeric()])
  lst = [letters, int(nums)]
  return (lst)

