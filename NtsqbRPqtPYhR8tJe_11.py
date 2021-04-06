
def blocks(step):
  num, blocks = 5, []
  lst = [i for i in range(step)]
  if not step:
    return 0
  for i in lst:
    if i == 0:
      blocks.append(num)
    else:
      if i > 0:
        blocks.append(((num + blocks[i-1]) + i)+1)
  return blocks[-1]

