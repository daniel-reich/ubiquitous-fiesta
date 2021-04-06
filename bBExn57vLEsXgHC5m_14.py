
def same_line(lst):
​
    x_coords = [point[0] for point in lst]
    y_coords = [point[1] for point in lst]
    
    try:
        y_deltas = (y_coords[2] - y_coords[0]) / (y_coords[1] - y_coords[0])
        x_deltas = (x_coords[2] - x_coords[0]) / (x_coords[1] - x_coords[0])
        return y_deltas == x_deltas
    
    except ZeroDivisionError:
        if len(set(x_coords)) == 1 or len(set(y_coords)) == 1:
            return True
        return False

