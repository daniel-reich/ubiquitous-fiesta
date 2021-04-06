
def champions(teams):
    z = list(zip(*[[team["name"],3*team["wins"]+team["draws"], team["scored"]-team["conceded"]] for team in teams]))
    m1_pos = [i for i, e in enumerate(z[1]) if e==max(z[1])]
    return z[0][z[1].index(max(z[1]))] if len(m1_pos)==1 else z[0][z[2].index(max(z[2][m1_pos[0]], z[2][m1_pos[1]]))]

