
from string import ascii_lowercase
from textwrap import wrap
​
def _create_polybius(keyword):
  result = ""
  for c in keyword[:25]:
    c = "i" if c == "j" else c
  
    if c not in result:
      result += c
​
  for c in ascii_lowercase:
    if len(result) == 25:
      break
​
    if c not in result and c != "j":
      result += c
​
  return wrap(result, 5)
​
def _insert_x_and_shift(diagraphs):
  for i in range(len(diagraphs)):
    d = diagraphs[i]
    if len(set(d)) != 2:
      diagraphs[i] = d[0] + "x" + (d[1] if len(d) == 2 else "")
      break
​
  return wrap("".join(diagraphs), 2)
​
def _polybius_find(polybius, val):
  return [(ix, iy) for ix, row in enumerate(polybius) for iy, i in enumerate(row) if i == val][0]
​
def _encrypt(txt, polybius):
  txt = "".join(c for c in txt if c.isalpha()).lower()
​
  diagraphs = wrap(txt, 2)
  while not all(len(set(d)) == 2 for d in diagraphs):
    diagraphs = _insert_x_and_shift(diagraphs)
​
  result = ""
  for i, j in diagraphs:
    i = "i" if i == "j" else i
    j = "i" if j == "j" else j
​
    i_row, i_col = _polybius_find(polybius, i)
    j_row, j_col = _polybius_find(polybius, j)
​
    if i_row == j_row:
      result += polybius[i_row][(i_col + 1) % 5] + polybius[i_row][(j_col + 1) % 5]
    elif i_col == j_col:
      result += polybius[(i_row + 1) % 5][i_col] + polybius[(j_row + 1) % 5][i_col]
    else:
      result += polybius[i_row][j_col] + polybius[j_row][i_col]
​
  return result.upper()
​
def _decrypt(txt, polybius):
  diagraphs = wrap(txt.lower(), 2)
​
  result = ""
  for i, j in diagraphs:
    i = "i" if i == "j" else i
    j = "i" if j == "j" else j
​
    i_row, i_col = _polybius_find(polybius, i)
    j_row, j_col = _polybius_find(polybius, j)
​
    if i_row == j_row:
      result += polybius[i_row][i_col - 1] + polybius[i_row][j_col - 1]
    elif i_col == j_col:
      result += polybius[i_row - 1][i_col] + polybius[j_row - 1][i_col]
    else:
      result += polybius[i_row][j_col] + polybius[j_row][i_col]
​
  return result.upper()
​
def playfair(txt, keyword):
  polybius = _create_polybius(keyword)
  return _decrypt(txt, polybius) if txt.isupper() else _encrypt(txt, polybius)

