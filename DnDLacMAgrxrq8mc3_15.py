
def blah_blah(t, n):
    return " ".join(t.split()[:-n] + ["blah"] * min(n, len(t.split()))) + "..."

