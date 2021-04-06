
import re
def count_lone_ones(n):
  return len([i for i in re.split('[02-9]', str(n)) if i == '1'])

