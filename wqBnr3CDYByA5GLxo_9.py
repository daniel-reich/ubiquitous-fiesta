
def unravel(txt):
    open_bracket, close_bracket = [], []
    for i in range(len(txt)):
        if txt[i] == '[':
            open_bracket.append(i)
        elif txt[i] == ']':
            close_bracket.append(i)
    sub_strings = []
    for o, c in zip(open_bracket, close_bracket):
        sub_strings.append(txt[o: c + 1])
    for i in range(len(sub_strings)):
        txt = txt.replace(sub_strings[i], '{}')
        sub_strings[i] = sub_strings[i].replace('[', "['")\
            .replace(']', "']").replace('|', "','")
    format_str, for_str = '', ''
    for i in range(len(sub_strings)):
        format_str += 's' + str(i) + ', '
        for_str += ' for ' + 's' + str(i) + ' in ' + sub_strings[i]
    return sorted(eval('["' + txt + '".format(' + format_str[: -2]
                  + ')' + for_str + ']'))

