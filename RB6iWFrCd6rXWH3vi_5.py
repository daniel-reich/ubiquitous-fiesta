
odd = {str(x) for x in (1,3,5,7,9)}
even = {str(x) for x in (0,2,4,6,8)}
​
def longest_substring(s):
    assert len(s) > 0
    curr_seq = s[0]
    last_odd = s[0] in odd
    longest_seq = ''
    for c in s[1:]:
        if (c in odd) != last_odd:
            curr_seq += c
        else:
            if len(curr_seq) > len(longest_seq):
                longest_seq = curr_seq
            curr_seq = c
        last_odd = c in odd
    if len(curr_seq) > len(longest_seq):
        longest_seq = curr_seq
​
    return longest_seq

