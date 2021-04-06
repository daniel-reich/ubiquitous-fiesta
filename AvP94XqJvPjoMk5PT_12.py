
def unique_styles(albums):
    result = 1
    new_albums = []
    for item in albums:
        temp = item.split(',')
        new_albums.extend(temp)
    for i,item in enumerate(new_albums):
        if i != 0 and item not in new_albums[:i]:
            result += 1
    return result

