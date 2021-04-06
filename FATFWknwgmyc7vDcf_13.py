
import re
def small_favor(sentence):
  if 'Fakemonthy' not in sentence:
    p=r'([0-3][0-9][\/\.][0-1][0-9][\/\.])([0-9]{2})'
    q=r'([A-Z]\w*[ary|er|ch|st|ne|ril|ay|ly]\,\s[0-1][0-9]\.\s)([0-9]{2})'
    sentence=re.sub(p, lambda m:m.group(1)+'19'+m.group(2) if int(m.group(2))>=25 else m.group(1)+'20'+m.group(2), sentence)
    sentence=re.sub(q, lambda m:m.group(1)+'19'+m.group(2) if int(m.group(2))>=25 else m.group(1)+'20'+m.group(2), sentence)
    return sentence
  else:
    return sentence
  # GL HF

