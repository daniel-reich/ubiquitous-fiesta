
def format_phone_number(lst):
  return (lambda chars: '({0}) {1}-{2}'.format(
    ''.join(chars[:3]),
    ''.join(chars[3:6]),
    ''.join(chars[6:])))([str(c) for c in lst])

