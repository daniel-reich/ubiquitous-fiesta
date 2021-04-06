
def can_complete(orig, complete):
    """
    Check if characters can be added to the first string to make the second string
​
    >>> can_complete("butl", "beautiful")
    True
​
    >>> can_complete("butlz", "beautiful")
    False
​
    >>> can_complete("tif", "beautiful")
    True
​
    >>> can_complete("tulb", "beautiful")
    False
​
    >>> can_complete("bbutl", "beautiful")
    False
    """
    for c in orig:
        idx = complete.find(c)
        if idx == -1:
            return False
        complete = complete[idx + 1:]
    return True

