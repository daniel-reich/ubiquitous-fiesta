
def count_repetitions(lst):
    return dict(sorted({x: lst.count(x) for x in lst}.items(), key=lambda x: x[1], reverse=True))

