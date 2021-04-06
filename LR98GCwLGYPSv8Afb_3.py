
from collections import*
pluralize=lambda l:{k+('','s')[v>1]for k,v in Counter(l).items()}

