
from collections import Counter
​
def will_fit(holds, cargo):
    C = Counter(holds) 
    total = 200 * C.get('L', 0) + 100 * C.get('M', 0) + 50 * C.get('S', 0)
    return sum(cargo) <= total

