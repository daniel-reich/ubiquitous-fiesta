
import re
def best_friend(txt, a, b):
  # Patern
  P = re.compile(a+b); # makes string e.g "he"
  # Find all cases of "he"
  X = re.findall(P,txt);
  # Find out if all cases "X" is equal to how many "h" are in string
  return len(X) == txt.count(a);

