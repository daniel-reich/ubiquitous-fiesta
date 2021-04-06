
def check_flush(deck):
    if len(set([x[-1] for x in deck])) == 1:
        return True
​
​
def check_straight(deck):
    numbers = [int(x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for x in deck]
    numbers.sort()
    if (numbers[4] - numbers[0]) == 4:
        return True
    return False
​
​
def check_royal(deck):
    numbers = [int(x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14')) for x in deck]
    if 14 in numbers:
        return True
    return False
​
​
def check_four_of_a_kind(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 4:
        return True
    return False
​
​
def check_full_house(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 3 and min(counts) == 2:
        return True
    return False
​
​
def check_three_of_a_kind(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 3:
        return True
    return False
​
​
def check_two_pair(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 2 and len(set(numbers)) == 3:
        return True
    return False
​
​
def check_pair(deck):
    numbers = [x[:-1].replace('J', '11').replace('Q', '12').replace('K', '13').replace('A', '14') for x in deck]
    counts = [numbers.count(x) for x in numbers]
    if max(counts) == 2:
        return True
    return False
​
​
def poker_hand_ranking(deck):
    if check_flush(deck):
        if check_straight(deck):
            if check_royal(deck):
                return "Royal Flush"
            else:
                return "Straight Flush"
        else:
            return "Flush"
    elif check_four_of_a_kind(deck):
        return "Four of a Kind"
​
    elif check_full_house(deck):
        return "Full House"
​
    elif check_straight(deck):
        return "Straight"
​
    elif check_three_of_a_kind(deck):
        return "Three of a Kind"
​
    elif check_two_pair(deck):
        return "Two Pair"
​
    elif check_pair(deck):
        return "Pair"
​
    else:
        return "High Card"

