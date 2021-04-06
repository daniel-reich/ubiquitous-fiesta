
from itertools import zip_longest
def nico_cipher(message, key):
  stacks = [([], char) for char in key]
  for idx, char in enumerate(message):
    stack_idx = idx % len(key)
    stacks[stack_idx][0].append(char)
  stacks.sort(key=lambda s: ord(s[1]))
  rows = []
  for row in zip_longest(*[s[0] for s in stacks], fillvalue=' '):
    rows.append(''.join(row))
  return ''.join(rows)

