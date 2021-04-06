
from math import pi, sin, cos
def hit_prince(vo, th, yo, ds, g=9.81):
    v_vertical, v_horizontal = vo * sin(pi / 180 * th), vo * cos(pi / 180 * th)
    t_up = v_vertical / g
    y1 = v_vertical * t_up - g * t_up * t_up / 2
    t_down = pow(2 * (yo + y1) / g, 0.5)
    d_shoot = v_horizontal * (t_up + t_down)
    return abs(d_shoot - ds) < 0.5

