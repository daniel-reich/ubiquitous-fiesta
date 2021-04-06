
import re
def inflect(verb, person, number):
  p=r'are|ere|ire'
  t=re.search(p,verb).group()[0]
  verb=re.sub(p,'',verb)
  pro=pronomi[person][number]
  spec=verbi_spec[person][number][0 if t=='a' else 1 if t=='e' else 2]
  com=verbi_com[person][number]
  res=pro+' '+verb+spec+com
  return res

