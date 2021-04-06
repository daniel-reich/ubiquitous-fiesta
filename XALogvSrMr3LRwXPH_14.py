
from re import search
is_shuffled_well = lambda r: search(r'11', ''.join(str
    (abs(x-r[i])) for i, x in enumerate(r[1:]))) is None

