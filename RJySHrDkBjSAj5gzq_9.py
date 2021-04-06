
import math
def nespers(lst):
    global ans
    ans = 1
    get_lens(lst)
    return ans
​
def get_lens(lst):
    if not lst:
        return 
    global ans
    ans = ans * (math.factorial(len(lst)))
    for e in lst:
        if type(e) == list:
            get_lens(e)
    return

