
from re import search
is_undulating = lambda n: bool(search(r'\A(\d)(\d)\1(\2\1)*\2?\Z', str(n)))

