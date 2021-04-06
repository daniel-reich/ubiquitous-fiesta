
def split_into_buckets(phrase, n):
    s = []
    if (max([len(x) for x in phrase.split()])) > n:
        return []
    while len(phrase) > 0:
        i = min(n, len(phrase))
        if i == len(phrase):
            s.append(phrase)
            return s
        while phrase[i] != " ":
            i -= 1
        s.append(phrase[: i])
        phrase = phrase[i + 1 :]

