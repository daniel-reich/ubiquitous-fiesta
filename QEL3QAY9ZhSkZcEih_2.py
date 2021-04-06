
import re
is_odd=lambda n:('No','Yes')[n&1]
is_even=lambda n:'Yes'if re.search('[02468]$',n)else'No'

