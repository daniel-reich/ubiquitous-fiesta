
from itertools import*
meme_sum=lambda a,b:int(''.join(str(int(x)+int(y))[::-1]for x,y in zip_longest(str(a)[::-1],str(b)[::-1],fillvalue='0'))[::-1])

