
def remove_leading_trailing(n):
  n = n.split('.')
  return '.'.join([n[0].lstrip('0') or '0', n[1].rstrip('0')]) \
        if len(n) == 2 and n[1].rstrip('0') else n[0].lstrip('0') \
        if n[0].lstrip('0') else '0'

