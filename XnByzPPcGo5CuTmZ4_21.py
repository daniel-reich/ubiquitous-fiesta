
def kix_code(addr):
  import re
  pattern= re.compile(r'\d[^,]{0,6}[\d\w]')
  part1, part2 = re.findall(pattern, addr.upper())
  return re.sub(r'\s','',part2)+re.sub(r'[^\d\w]','X', part1)

