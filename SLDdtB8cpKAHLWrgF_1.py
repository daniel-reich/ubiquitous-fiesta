
import re
def greater_permutation(expr, nums):
    expstr = re.sub('[abc]', '{}', expr)
    mx, mxe = -2**15, ''
    for a,b,c in [(0,1,2), (0,2,1), (1,0,2), (1,2,0), (2,0,1), (2,1,0)]:
        s = expstr.format(nums[a], nums[b], nums[c])
        val = eval(s)
        if val>mx:
            mx, mxe = val, s
    return "{} = {}".format(mxe, round(mx, 2) if mx%1 else int(mx))

