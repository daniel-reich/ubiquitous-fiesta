
import re
def same_letter_pattern(txt1, txt2):
  t1 = sorted(set(txt1), key=txt1.index)
  t2 = sorted(set(txt2), key=txt2.index)
  for i, a, b in zip(range(len(t1)), t1, t2):
    txt1 = re.sub(a, str(i), txt1)
    txt2 = re.sub(b, str(i), txt2)
  return txt1 == txt2

