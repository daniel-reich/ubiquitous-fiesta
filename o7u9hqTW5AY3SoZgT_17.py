
import re
switcheroo = lambda x: ' '.join(w.replace('nts', 'nce') if re.search('nts$', re.sub('[^a-z]', '', w))
  else w.replace('nce', 'nts') if re.search('nce$', re.sub('[^a-z]', '', w)) else w for w in x.split())

