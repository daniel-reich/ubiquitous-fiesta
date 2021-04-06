
import numpy as np
​
def how_close_to_c(rapidity):
    one_minus_beta = 1 / np.cosh(2 * rapidity)
    ans = format("%.2e" % one_minus_beta)
    while "-0" in ans:
        ans = ans.replace("-0", "-")
    return ans

