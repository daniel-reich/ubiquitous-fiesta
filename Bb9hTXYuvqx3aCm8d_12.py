
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    player_A, player_Z = 0, 0
    str_A = eliminate(str_A, ind_Z)
    str_Z = eliminate(str_Z, ind_A)
    str_A = ascii_values(str_A)
    str_Z = ascii_values(str_Z)
    for a, z in zip(str_A, str_Z):
        if a > z:
            player_A += abs(a - z)
        else:
            player_Z += abs(a - z)
    return {"A" : player_A, "Z" : player_Z}    
    
def ascii_values(string):
    return [ord(x) for x in string]
​
def eliminate(string, index):
    for x in index:
        string = string.replace(string[x], " ")
    string = "".join(string.split())
    return string

