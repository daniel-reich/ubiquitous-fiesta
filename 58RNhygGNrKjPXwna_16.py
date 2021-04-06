
def longest_nonrepeating_substring(txt):
    longest_string = ''
    current_string = ''
    for i in range(len(txt)):
        for x in txt[i:]:
            if x not in current_string:
                current_string+=x
            else:
                current_string = ''
                break
            if len(current_string) > len(longest_string):
                longest_string = current_string
    return longest_string

