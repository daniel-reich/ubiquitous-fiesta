
def percentage_changed(old, new):
    num_new = int(new[1:])
    num_old = int(old[1:])
    changed = int(num_new - num_old)
    changed_percentage = abs(round((changed / num_old) * 100))
​
    if num_old > num_new:
        return "{}% decrease".format(changed_percentage) 
    elif num_old < num_new:
        return "{}% increase".format(changed_percentage)

