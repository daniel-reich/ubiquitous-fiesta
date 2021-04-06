
def points_in_circle(points, centerX, centerY, radius):
    x = []
    y = []
    result = []
​
    for i in points:
        for key, value in i.items():
            if key == "x":
                x.append(value)
            if key == "y":
                y.append(value)
    for i in range(0, len(x)):
        distance = (((centerX-x[i])**2) + (centerY-y[i])**2)**0.5
        if distance < radius:
            result.append(distance)
    return len(result)

