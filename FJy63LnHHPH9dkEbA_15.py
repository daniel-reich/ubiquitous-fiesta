
import math
def how_close_to_c(rapidity):
    ans = 1/(math.cosh(2*rapidity))
    ans_scientific =  "{:.2e}".format(float(ans))
    ans_scientific_parts = ans_scientific.partition("-")
    if ans_scientific_parts[2][0] == "0":
        return ans_scientific[0:len(ans_scientific)-2] + ans_scientific[len(ans_scientific)-1 : len(ans_scientific)]
    else:
        return ans_scientific

