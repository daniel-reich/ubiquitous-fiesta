
def unique_styles(albums):
    ans = set()
    for s in albums:
        for style in s.split(','):
            ans.add(style)
    return len(ans)

