
def unique_styles(albums):
    unique = []
    for genres in albums:
        for genre in genres.split(','):
            unique.append(genre)
​
    return len(set(unique))

