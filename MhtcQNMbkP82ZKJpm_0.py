
from collections import *
get_notes_distribution=lambda s:Counter(y for x in s for y in x['notes']if y in(1,2,3,4,5))

