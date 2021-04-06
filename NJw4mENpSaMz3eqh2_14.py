
def is_undulating(n: int) -> bool:
    return len(str(n)) >= 3 and len(set(str(n))) == 2 and len(set(str(n)[::2])) == 1 \
           and len(set(str(n)[1::2])) == 1

