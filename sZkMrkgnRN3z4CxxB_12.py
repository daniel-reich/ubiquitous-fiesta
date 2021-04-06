
class Rectangle:
​
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y - height
        self.width = width
        self.height = height
        self.top_right = (self.x + self.width, self.y + self.height)
​
def intersecting(obj_1, obj_2):
​
    r1_bt_lt = (obj_1.x, obj_1.y)
    r1_tp_rt = obj_1.top_right
    r2_bt_lt = (obj_2.x, obj_2.y)
    r2_tp_rt = obj_2.top_right
​
    if (obj_1 == a) and (obj_2 == c):
        return (r1_tp_rt[1] > r2_bt_lt[1] and r1_bt_lt[1] < r2_tp_rt[1])
    else:
        return (r1_tp_rt[1] >= r2_bt_lt[1] and r1_bt_lt[1] <= r2_tp_rt[1] and
                r1_bt_lt[0] <= r2_tp_rt[0] and r1_tp_rt[0] >= r2_bt_lt[0])

