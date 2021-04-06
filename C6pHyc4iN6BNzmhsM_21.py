
import collections
​
Card = collections.namedtuple("Card", "num suit")
d = {'2': 2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":11, "Q":12, "K":13, "A":14}
​
def poker_hand_ranking(deck):
    deck = [Card(item[:-1], item[-1]) for item in deck]
    suit_counter = collections.Counter([card.suit for card in deck])
    num_counter = collections.Counter([card.num for card in deck])
    nums = [d[card.num] for card in deck]
    print(sorted(nums))
    if flush(suit_counter) and royal(nums):
        return "Royal Flush"
    elif flush(suit_counter) and straight(nums):
        return "Straight Flush"
    elif four_of_a_kind(num_counter):
        return "Four of a Kind"
    elif full_house(num_counter):
        return "Full House"
    elif flush(suit_counter):
        return "Flush"
    elif straight(nums):
        return "Straight"
    elif three_of_a_kind(num_counter):
        return "Three of a Kind"
    elif two_pair(num_counter):
        return "Two Pair"
    elif two_of_a_kind(num_counter):
        return "Pair"
    else:
        return "High Card"
        
def flush(suit_counter):
    return 5 in suit_counter.values()
​
def four_of_a_kind(num_counter):
    return 4 in num_counter.values()
​
def full_house(suit_counter):
    return sorted(suit_counter.values()) == [2, 3]
​
def three_of_a_kind(num_counter):
    return 3 in num_counter.values()
​
def two_pair(num_counter):
    return sorted(num_counter.values()) == [1, 2, 2]
​
def two_of_a_kind(num_counter):
    return sorted(num_counter.values()) == [1, 1, 1, 2]
​
def royal(nums):
    return sorted(nums) == [10, 11, 12, 13, 14]
​
def straight(nums):
    order = [i for i in range(2, 15)]
    return sorted(nums) in [order[n:n+5] for n in range(9)]

