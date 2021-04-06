
def count_repetitions(lst):
    return {e: lst.count(e) for e in set(lst)}

