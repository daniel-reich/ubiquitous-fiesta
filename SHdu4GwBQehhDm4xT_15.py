
def freed_prisoners(prison):
    freed = 0
    if prison[0] == 0:
        return freed
    else:
        for i in range(len(prison)):
            if prison[i] == 1:
                freed += 1
                prison = list(map(lambda x: 1 if x == 0 else 0, prison))
    return freed

