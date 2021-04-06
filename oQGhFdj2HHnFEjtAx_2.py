
def slicer(s, q, z=True, x=False):
    p, w, t = [s.find(i) for i in q], "[", len(s) - z
    if len(p) == z: return str(p)
    j, f, a = p[z] - p[x], p[x], p[-z]; d = z if j > x else -z
    w += str(f) if f != x and f != t else ""
    w += (":" + str(a + d)) if x <= a + j <= t else ":"
    return w+((":" + str(j)) if j != z else "") + "]"

