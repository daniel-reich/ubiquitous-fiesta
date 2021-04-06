
card_values = {"A": 11, "K": 10, "Q": 10, "J": 10}
​
def over_twenty_one(cards) -> bool:
    """Determine if sum is over 21."""
    total = None
    total = sum([card_values.get(x, x) for x in cards])
    if total <= 21:
        return False
    if ("A" in cards) and (total - 10 <= 21):
        return False
    return True

