
def apocalyptic(n):
    number = pow(2,n)
    number = str(number)
    if len(number) >= 3:
        for i in range(len(number)-3):
            if number[i:(i+3)] == "666":
                return "Repent! " + str(i) + " days until the Apocalypse!"
    return "Crisis averted. Resume sinning."

