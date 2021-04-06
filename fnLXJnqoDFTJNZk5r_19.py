
def sort_contacts(names, sort):
    if names is None:
        return []
    if sort == "ASC":
        names = sorted(names, key=lambda x: x.split()[-1])
    else:
        names = sorted(names, key=lambda x: x.split()[-1], reverse=True)
    return names

