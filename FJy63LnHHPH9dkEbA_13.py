
import math
def how_close_to_c(rapidity):
    ans = '{:.2e}'.format(1 / math.cosh(2 * rapidity)).split('-')
    ans[1]=str(int(ans[1]))
    return '-'.join(ans)

