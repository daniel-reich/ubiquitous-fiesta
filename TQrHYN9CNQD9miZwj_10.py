
def fix_import(s):
  part1 = s[s.find('from'):]
  part2 = s[s.find('import'): s.find('from')-1]
  return "%s %s" % (part1, part2)

