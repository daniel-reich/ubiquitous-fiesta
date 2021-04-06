
def crop_hydrated(f):
    for r in range(len(f)):
        for c in range(len(f[r])):
            if f[r][c] == "c":
                if not any([
                    f[r][min(c + 1, len(f[r]) - 1)] == "w",
                    f[r][max(c - 1, 0)] == "w",
                    f[min(r + 1, len(f) - 1)][c] == "w",
                    f[max(r - 1, 0)][c] == "w",
                    f[min(r + 1, len(f) - 1)][min(c + 1, len(f[r]) - 1)] == "w",
                    f[min(r + 1, len(f) - 1)][max(c - 1, 0)] == "w",
                    f[max(r - 1, 0)][min(c + 1, len(f[r]) - 1)] == "w",
                    f[max(r - 1, 0)][max(c - 1, 0)] == "w"
                    ]):
                        return False
                     
    return True

