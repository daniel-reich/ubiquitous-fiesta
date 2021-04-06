
import numpy as np
​
def digital_division(n):
    digits = [int(i) for i in str(n)]
    test1 = all(n%d == 0 for d in digits if d != 0)
    test2 = n%sum(digits) == 0
    test3 = False if 0 in digits else n%np.prod(digits) == 0
​
    passed = sum((test1, test2, test3))
    return {3: 'Perfect', 0: 'Indivisible'}.get(passed, passed)

