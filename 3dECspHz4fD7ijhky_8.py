
def numbers_range(ranges):
  if len(ranges) < 2:
    return str(ranges[0]) if ranges else ''
  ranges.append(.1)
  a, b = 0, 0
  parts = []
  while b < len(ranges) - 1:
    if ranges[b] + 1 == ranges[b + 1]:
      b += 1
    else:
      parts.append((a, b))
      b += 1
      a = b
  str_ranges = []
  for a, b in parts:
    if b - a == 0:
      str_ranges.append(str(ranges[a]))
    elif b - a == 1:
      str_ranges.append(str(ranges[a]) + ', ' + str(ranges[b]))
    else:
      str_ranges.append(str(ranges[a]) + '-' + str(ranges[b]))
  return ', '.join(str_ranges)

