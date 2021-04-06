
points_in_circle = lambda points, centerX, centerY, radius: len([i for i in points if (i["x"] - centerX) ** 2 + (i["y"] - centerY) ** 2 < radius ** 2])

