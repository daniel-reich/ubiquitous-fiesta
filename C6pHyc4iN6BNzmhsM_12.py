
def get_n(hand):
  return list(map(lambda x: x[:-1], hand))
​
def royal(hand):
  return flush(hand) and ['10','A','J','K','Q'] == sorted(get_n(hand))
​
def s_f(hand):
  return st(hand) and flush(hand)
​
def flush(hand):
  return all(hand[i][-1] == hand[i-1][-1] for i in range(5))
​
def st(hand):
  order = ["2","3","4","5","6","7","8","9","10","J","Q","K","A"]
  hand = sorted(get_n(hand), key=lambda x: order.index(x))
  if ["10","J","Q","K","A"] == hand: return True
  return all(order.index(hand[0])+i == order.index(hand[i]) for i in range(4))
​
def n_kind(hand, n):
  return any(get_n(hand).count(get_n(hand)[x]) == n for x in range(4))
​
def f_h(hand):
  return n_kind(hand, 2) and n_kind(hand, 3)
​
def two_p(hand):
  d = {get_n(hand)[i]: get_n(hand).count(get_n(hand)[i]) for i in range(5)} 
  return list(d.values()).count(2) == 2
  
def poker_hand_ranking(h):
  l = [royal(h),s_f(h),n_kind(h,4),f_h(h),flush(h),st(h),n_kind(h,3),two_p(h),n_kind(h,2),True]
  returns = ["Royal Flush", "Straight Flush", "Four of a Kind", "Full House",\
  "Flush", "Straight", "Three of a Kind", "Two Pair", "Pair", "High Card"]
  return [returns[x] for x in range(len(l)) if l[x] == True][0]

