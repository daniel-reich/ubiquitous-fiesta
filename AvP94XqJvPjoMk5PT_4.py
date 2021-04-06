
def unique_styles(albums):
    return len(set(sum([g.split(',') for g in albums], [])))

