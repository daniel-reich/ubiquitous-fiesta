
def final_direction(direction, lst) -> str:
    directions = ('N', 'E', 'S', 'W')
    change = sum(1 if i == 'R' else -1 for i in lst)
    return directions[(directions.index(direction) + change) % 4]

