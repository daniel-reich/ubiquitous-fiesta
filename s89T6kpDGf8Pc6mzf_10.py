
digits_to_letters = {
    '0': 'abcdef', '1': 'bc', '2': 'abdeg', '3': 'abcdg', '4': 'bcfg',
    '5': 'acdfg', '6': 'acdefg', '7': 'abc', '8': 'abcdefg', '9': 'abcfg'
}
​
​
def seven_segment(txt):
    if len(txt) == 1:
        return []
    res = []
    current = txt[0]
    for i in range(1, len(txt)):
        if txt[i] == current:
            res.append([])
        else:
            current_state = digits_to_letters[current]
            new_state = digits_to_letters[txt[i]]
            digits_off = [c for c in (set(current_state) - set(new_state))]
            digits_on = [c.upper() for c in (set(new_state)
                                             - set(current_state))]
            res.append(sorted(digits_on + digits_off, key=lambda x: x.lower()))
        current = txt[i]
    return res

