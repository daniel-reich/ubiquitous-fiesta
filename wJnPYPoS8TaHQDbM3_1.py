
from itertools import*
dice_roll=lambda n,m:sum(m==sum(x)for x in product(range(1,7),repeat=n))

