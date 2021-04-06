
def bacteria(final_mass):
    mass, bacter, count = 1, 1, 0
    while mass != final_mass:
        massa = mass
        bacterias = bacter
        if massa + 4*bacterias <= final_mass:
            mass += 2*bacterias
            bacter = 2*bacterias
            count += 1
        else:
            valor = final_mass - massa
            if valor//bacterias == 1:
                bacter = (bacterias + valor % bacterias)
                count += 1
                mass += bacter
            elif valor//bacterias == 2:
                if valor % bacterias == 0:
                    mass = final_mass
                    bacter = (2*bacterias)
                    count += 1
                else:
                    mass += bacterias
                    bacter = (bacterias + valor % bacterias)
                    count += 2
                    mass += bacter
            elif valor//bacterias == 3:
                count += 2
                mass = final_mass
    return count

