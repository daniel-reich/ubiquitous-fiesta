
def time_to_finish(full, part):
    return sum(len(w) for w in full.replace(part, '').split()) * 0.5

