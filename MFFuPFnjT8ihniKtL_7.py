
def bug_jump(h, t):
    '''
    Returns the position of the bug after time t msecs, and its direction of
    travel as per instructions, given its maximum height is h cm.
    '''
    a, b, c = -1, 6, 0  # vanilla graph: y = -t^2 +6t
    v_max = 9  # h for the original graph, y coordinate of the vertex
    t /= 1000  # convert to secs
    k = 0      # for the horizontal translation
    mid = 3    # the x coordinate for the vanilla graph vertex
​
    if h != v_max:
        c = h - v_max  # the vertical translation
        x1 = (-b + (b*b - 4 * a * c)**0.5) / (2 * a)
        x2 = (-b - (b*b - 4 * a * c)**0.5) / (2 * a)
        k = min(abs(x1), abs(x2))  # lowest root
        
        if h < v_max:
            k = -k  # shifting left so add
​
    pos = round(-(t - k)**2 + b * (t - k) + c, 2)
    
    return [0, None] if pos < 0 else \
           [pos, 'up'] if t < mid + k else \
           [pos, 'down']

