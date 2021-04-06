
def is_rectangle(nums):
    temp_listing = [number for number in nums]
    coord = []
    coordinates = []
    lines = []
    filtered_lines = []
    a = []
    for number in temp_listing:
        number1 = (number.strip('('))
        number1 = (number1.strip(')'))
        coord.append(number1)
    for coordinate in coord:
        coordinates.append(coordinate.split(","))
    for index in range(0,len(coordinates)):
        if index == len(coordinates)-1:
            x = abs(int(coordinates[index][0]) - int(coordinates[0][0]))
            y = abs(int(coordinates[index][1]) - int(coordinates[0][1]))
            line = (x**2) + (y ** 2)
            lines.append(line)
        else:
            x = abs(int(coordinates[index][0]) - int(coordinates[index+1][0]))
            y = abs(int(coordinates[index][1]) - int(coordinates[index+1][1]))
            line = (x**2) + (y ** 2)
            lines.append(line)
    
    for count in range(0,len(lines)):
        if count == len(lines)-1:
            adjacent = ((lines[count])**2 + (lines[0])**2)
            filtered_lines.append(adjacent)
        else:
            adjacent = ((lines[count])**2 + (lines[count+1])**2)
            filtered_lines.append(adjacent)
        
    if len(filtered_lines) != 4:
        return False
    else:
        for lining in filtered_lines:
            if lining not in a:
                a.append(lining)
    if len(a) != 1:
        return False
    else:
        return True

