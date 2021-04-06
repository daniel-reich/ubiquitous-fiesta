
def fruit_salad(fruits):
    chunks = []
    for f in fruits:
        idx = len(f) // 2
        chunks.append(f[: idx])
        chunks.append(f[idx:])
    return "".join(sorted(chunks))

