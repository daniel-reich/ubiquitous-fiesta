
def nico_cipher(message, key): 
  cols = [
    (c, [
      message[i + j * len(key)]
      if i + j * len(key) < len(message) else ' '
      for j in range(len(message) // len(key) + 1)
    ])
    for i, c in enumerate(key)
  ]
​
  sorted_cols = [col[1] for col in sorted(cols, key=lambda x: x[0][0])]
​
  return ''.join(sum([
    [sorted_cols[i][j] for i in range(len(key))]
    for j in range(len(message) // len(key) + 1)
  ], []))

