
def longest_nonrepeating_substring(string):
    start = end  = 0 
    out = final = ''
    frequency = set()
    while start < len(string):
        if end < len(string) and string[end] not in frequency:
            out += string[end]
            final = max(final, out, key=len)
            frequency.add(string[end])
            end += 1
        else:
            frequency.discard(string[start])
            out = out[1:]
            start += 1
    return final

