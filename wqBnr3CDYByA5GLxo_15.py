
import re
def unravel(txt):
    x = re.search(r'\[([^\[\]]+(\|[^\[\]]+)*)\]', txt)
    if not x: return [txt]
    options, chained = x.group(1).split('|'), []
    for option in options:
        chained += unravel(txt[:x.start()] + option + txt[x.end():])
    return list(sorted(chained))

