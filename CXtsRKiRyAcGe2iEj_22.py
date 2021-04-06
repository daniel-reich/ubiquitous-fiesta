
def time_to_finish(full, part):
    a = full.replace(' ','')
    b = part.replace(' ','')
    ca = 0
    cb = 0
    for i in a:
        ca += 1
    for i in b:
        cb += 1
    return (ca-cb)*0.5

