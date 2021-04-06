
def isbn13(txt):
  if len(txt) == 10 and not sum_isbn_10(txt) % 11:
    for i in range(10):
      if not sum_isbn_13('978' + txt[:-1] + str(i)) % 10:
        return  '978' + txt[:-1] + str(i)
  elif len(txt) == 13 and not sum_isbn_13(txt) % 10:
    return 'Valid'
  else:
    return 'Invalid'
def sum_isbn_10(txt):
  sum_ = sum(j * int(txt[i]) for i,j in zip(range(len(txt)),range(10,1,-1)))
  return sum_ + 10 if txt[-1] == 'X' else sum_ + int(txt[-1])
def sum_isbn_13(txt):
  return sum(3 * int(txt[i]) if i % 2 else 1 * int(txt[i]) for i in range(len(txt)))

