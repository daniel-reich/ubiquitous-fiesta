
def to_bit_string(time):
  bitmap = {"0": [7, 5, 5, 5, 7], "1": [2, 6, 2, 2, 7], "2": [7, 1, 7, 4, 7],
    "3": [7, 1, 7, 1, 7], "4": [5, 5, 7, 1, 1], "5": [7, 4, 7, 1, 7], "6": [4, 4, 7, 5, 7],
    "7": [7, 1, 1, 1, 1], "8": [7, 5, 7, 5, 7], "9": [7, 5, 7, 1, 1], ":": [0, 2, 0, 2, 0]}
  b = [[('00'+bin(s)[2:])[-3:] for s in x] for x in [bitmap[n] for n in time]]
  c = [[(k+'0') if not i else ('0'+k) if i == 4 else k for k in x] for i, x in enumerate(b)]
  return ''.join(''.join(list(x)) for x in zip(*c))

