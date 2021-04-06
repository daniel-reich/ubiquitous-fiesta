
import re
from collections import OrderedDict
sigilize = lambda s: re.sub(r"[aeiouAEIOU ]",'',''.join(OrderedDict.fromkeys(s[::-1]))).upper()[::-1]

