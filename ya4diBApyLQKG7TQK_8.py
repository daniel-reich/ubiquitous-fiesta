
import re
def validate_relationships(txt):
    nums = re.findall(r"[-]?\d+", txt)
    oper = iter("==" if o == "=" else o for o in re.findall(r"[<>=]\=?", txt))
    return all(eval(x+next(oper)+y) for x,y in zip(nums,nums[1:]))

