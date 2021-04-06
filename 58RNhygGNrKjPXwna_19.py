
def longest_nonrepeating_substring(txt):
    sub = list()
    for index, i in enumerate(txt):
        queue = i
        for j in txt[index + 1:]:
            if j not in queue:
                queue += j
            else:
                sub.append(queue)
                queue = j
        sub.append(queue)
    return max(sub, key=len)

