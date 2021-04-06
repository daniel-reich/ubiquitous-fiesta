
def unique_styles(albums=list):
    unique=[]
    for genres in albums:
        genre=genres.split(",")
        print(genre)
        for x in genre:
            if x not in unique:
                unique.append(x)
    return len(unique)

