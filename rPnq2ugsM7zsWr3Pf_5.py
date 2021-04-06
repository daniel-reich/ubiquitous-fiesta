
def find_all_digits(blocks, digits=''):
  if not blocks:
    return 'Missing digits!'
  digits = ''.join(sorted(set(digits+str(blocks[0]))))
  if len(digits) == 10:
    return blocks[0]
  return find_all_digits(blocks[1:], digits)

