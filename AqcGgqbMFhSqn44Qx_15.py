
def tweet(txt):
    import re
    solution = ""
    
    HandlesRegex = re.compile(r'(^|\s)(@|#)(\w*)')
    matches = HandlesRegex.findall(txt)
​
    for space, handle, text in matches:
        if len(solution) == 0:
            solution += handle+text
        elif len(solution) > 0:
            solution += ' '+handle+text
    return solution

