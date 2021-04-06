
def worm_length(worm):
    return "invalid" if any(x for x in worm if x != '-') or len(worm) == 0 else str(len(worm) *10)+" mm."

