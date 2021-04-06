
reorder_digits = lambda l, d: \
  [int(''.join(sorted(list(str(i)), reverse=d == "desc"))) for i in l]

