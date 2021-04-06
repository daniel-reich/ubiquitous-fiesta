
import re
def count_smileys(lst):
   return len(re.findall('[:;][-~]?[)D]', str(lst)))

