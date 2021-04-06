
def grant_the_hint(txt):
    lst = txt.split()
    lens = [len(w) for w in lst]
    return [(' '.join((w[:i] + '_' * lens[j])[:lens[j]]
                      for j, w in enumerate(lst)))
            for i in range(max(lens) + 1)]

