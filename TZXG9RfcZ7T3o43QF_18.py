
import re
def same_length(txt):
  pattern = r''
  for i in range(1,int(len(txt)/2)+1):
    c = r'1'*i+r'0'*i+r'|'
    pattern+=c
  pattern+=r'1'*(int(len(txt)/2)+1)+r'0'*(int(len(txt)/2)+1)
  return list(set(re.sub(pattern,'*',txt))) == ['*']

