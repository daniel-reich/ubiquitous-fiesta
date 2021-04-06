
def bracket_logic(xp):
    brackets, pos = '()<>[]{}', 0
    while pos < len(xp):
        if xp[pos] not in brackets:
            xp = xp[:pos] + xp[pos + 1:]
        else:
            pos += 1
    while '()' in xp or '<>' in xp or '[]' in xp or '{}' in xp:
        xp = xp.replace('()', '').replace('<>', '').replace('[]', '')\
            .replace('{}', '')
    return len(xp) == 0

