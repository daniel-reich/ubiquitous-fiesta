
import string
​
def bishop(start, end, n):
    alphabet = string.ascii_lowercase
​
    int_s, int_e = int(start[1]), int(end[1])
    i_s, i_e = alphabet.find(start[0])+1, alphabet.find(end[0])+1
    t = i_s + i_e + int_s + int_e
​
    if (t % 2) == 0:
        if start == end:
            return True
​
        if abs(i_e-i_s) == abs(int_s-int_e):
            if n > 0:
                return True
            else:
                return False
​
        if n > 1:
            return True
​
    return False

