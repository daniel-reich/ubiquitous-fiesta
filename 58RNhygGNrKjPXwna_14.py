
def longest_nonrepeating_substring(string):
    longest = []
    current = []
    for char in string:
        if len(current) > len(longest):
            longest = current
        while char in current:
            current = current[1:]
        current.append(char)
    return ''.join(str(char) for char in longest)

