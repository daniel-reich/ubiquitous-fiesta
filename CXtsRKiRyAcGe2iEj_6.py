
def time_to_finish(full, part):
    return len(list(i for i in full[len(part):] if i!=" "))*0.5

