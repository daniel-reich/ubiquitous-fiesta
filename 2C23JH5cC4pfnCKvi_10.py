
from collections import Counter
def check_flush(table, hand):
    is_flush = Counter()
    table.extend(hand)
    for card in table:
        temp = card.split("_")
        is_flush.update(temp[-1])
    return max(is_flush.values()) >= 5

