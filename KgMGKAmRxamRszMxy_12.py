
from math import ceil
def spartans_cipher(mess, n_Slide):
    col = ceil(len(mess) / n_Slide)
    mess = mess.ljust(n_Slide * col)
    return (''.join(j for i in range(col) for j in mess[i::col])).strip()

