
from typing import List
​
​
def flatten_the_curve(lst: List[int]) -> List[float]:
    if not lst:
        return []
    avg = round(sum(lst) / len(lst), 1)
    return [avg for _ in range(len(lst))]

