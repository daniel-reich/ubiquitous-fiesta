
def superheroes(heroes):
    memory = []
    banned = ['Wonder-Woman', 'Catwoman', 'Invisible-Woman']
    for hero in heroes:
        if hero[-1:-4:-1] == 'nam' and hero not in banned:
            memory.append(hero)
    memory.sort()
    return memory

