
import math
​
def format_ascii(txt, width):
    return '\n'.join([txt[k*width:k*width+width] for k in range(int(math.ceil(len(txt)) / float(width)))])

