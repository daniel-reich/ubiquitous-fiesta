
def babbage(n):
  root, c = n**0.5, 1
  while root != int(root):
    num = int(str(c)+str(n))
    c += 1
    root = num**0.5
  if n == 269696:
    return "Babbage was {}!".format(['incorrect', 'correct'][root == 99736])
  return root

