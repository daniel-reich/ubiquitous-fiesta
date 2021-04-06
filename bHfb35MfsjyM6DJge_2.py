
def route_diff(directions):
    pass
    pos = get_position(directions)
    
    return len(directions) - abs(pos[0]) - abs(pos[1])
​
def get_position(directions):
​
    ns_dir = 0
    ew_dir = 0
​
    for dir in directions:
​
        if dir == "N":
            ns_dir += 1
        elif dir == "S":
            ns_dir -= 1
        elif dir == "E":
            ew_dir += 1
        else:
            ew_dir -= 1
​
    return (ew_dir, ns_dir)
​
​
directions = ["N", "S", "N", "S", "E", "W", "E", "E"]
​
print(route_diff(directions))

