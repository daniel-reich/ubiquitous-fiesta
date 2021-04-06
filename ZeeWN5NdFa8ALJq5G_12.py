
def nearest_chapter(chapt, page):
    rev_chapt = {v: k for k, v in chapt.items()}
    if page in rev_chapt:
        return rev_chapt[page]
    if page < min(rev_chapt.keys()):
        return "Chapter 1"
    if page > max(rev_chapt.keys()):
        return rev_chapt[max(rev_chapt.keys())]
    low = 0
    for p in sorted(rev_chapt.keys()):
        if p < page:
            low = p
        elif p > page:
            high = p
            break
    return rev_chapt[high] if high - page <= page - low else rev_chapt[low]

