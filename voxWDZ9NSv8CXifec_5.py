
from heapq import *
def lemonade(bills):
    remain_heap = []
    for bill in bills:
        if bill == 5:
            heappush(remain_heap, bill)
        elif bill == 10:
            heappush(remain_heap, bill)
            if remain_heap[0] == 10 or remain_heap[0] == 20:
                return False
            else:
                heappop(remain_heap)
        elif bill == 20:
             heappush(remain_heap, bill)
             if sum(remain_heap[:-1]) < 15:
                 return False
             elif len(remain_heap) < 3:
                 return False
             elif len(remain_heap) >= 3:
                 pop_price_1 = heappop(remain_heap)
                 if pop_price_1 > 15:
                     return False
                 elif pop_price_1 <= 15:
                      pop_price_2 = heappop(remain_heap)
                      if pop_price_1 + pop_price_2 > 15:
                          return False
                      else:
                          pop_price_3 = heappop(remain_heap)
                          if pop_price_1 + pop_price_2 + pop_price_3> 35:
                              return False
​
    return True

