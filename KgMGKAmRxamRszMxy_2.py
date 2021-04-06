
from math import ceil
def spartans_cipher(msg, n):
    len_msg = len(msg)
    len_new = ceil(len_msg / n) * n
    cols = len_new // n
    msg += (len_new - len_msg) * " "
    lst_msg = [msg[i * cols: (i + 1) * cols] for i in range(n)]
    return "".join("".join(tpl) for tpl in zip(*lst_msg)).rstrip(" ")

