
from itertools import*
malthusian=lambda f,p:next((x for x in count()if 100*p**x>100+f*x))

