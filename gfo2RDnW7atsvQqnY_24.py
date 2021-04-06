
import re
def count_smileys(lst):
  return sum([1 for s in lst if bool(re.fullmatch('(:|;)(~|-)?(\)|D)', s))])

