
def abbreviate(st, n=4):
    return ''.join(map(lambda x: x[0].upper(),filter(lambda x: len(x) >= n, st.split())))

