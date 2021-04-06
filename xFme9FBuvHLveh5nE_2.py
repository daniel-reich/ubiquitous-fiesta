
from itertools import*
is_zygodrome=lambda n:all(len(list(g))>1for _,g in groupby(str(n)))

