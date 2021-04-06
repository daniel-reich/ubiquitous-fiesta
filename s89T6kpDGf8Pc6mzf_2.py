
def seven_segment(digits):
    '''
    Returns a list of sorted segment transition changes for the digits in
    digits, rules as above
    '''
    LIT_SEGS = {
                '0': 'abcdef',
                '1': 'bc',
                '2': 'abdeg',
                '3': 'abcdg',
                '4': 'bcfg',
                '5': 'acdfg',
                '6': 'acdefg',
                '7': 'abc',
                '8': 'abcdefg',
                '9': 'abcfg'
               }  # display segment mappings
​
    return [sorted(list(set(LIT_SEGS[b].upper()) - set(LIT_SEGS[a].upper())) + \
                   list(set(LIT_SEGS[a]) - set(LIT_SEGS[b])), key=lambda x: x.lower()) \
            for a, b in zip(digits, digits[1:])]

