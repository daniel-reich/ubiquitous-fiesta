
def max_occur(text):
    max_count, cnt = 1, dict()
    for c in text:
        if c in cnt:
            cnt[c] += 1
        else:
            cnt[c] = 1
        max_count = max(max_count, cnt[c])
    return (sorted(k for k, v in cnt.items() if v == max_count)
            if max_count > 1 else "No Repetition")

