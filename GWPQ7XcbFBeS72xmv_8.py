
def calculate_scores(txt):
    andy=0
    ben=0
    charlette=0
    if txt == '': return[0,0,0]
    for letter in txt:
        if letter == 'A': andy+=1
        if letter == 'B': ben+=1
        if letter == 'C': charlette+=1
    return [andy,ben,charlette]

