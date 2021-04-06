
def longest_substring(number):
    """
    Finds the longest substring with alternating odd and even digits
​
    >>> longest_substring("225424272163254474441338664823")
    '272163254'
​
    >>> longest_substring("594127169973391692147228678476")
    '16921472'
​
    >>> longest_substring("721449827599186159274227324466")
    '7214'
    """
    longest_substring = ""
    substring = ""
    last_parity = -1
    for d in number:
        digit_parity = int(d) % 2
        if last_parity != digit_parity:
            substring += d
            if (len(substring) > len(longest_substring)):
                longest_substring = substring
        else:
            substring = d
​
        last_parity = digit_parity
    return longest_substring

