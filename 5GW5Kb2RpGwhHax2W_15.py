
def width_height(array):
    h = len(array)
    w = len(array[0])
    return w,h
​
def spiral_transposition(array, rimx=0, rimy=0):
    w, h= width_height(array)
    max_rings = min(w, h)//2
    ring = list()
    ring += [array[rimy][x] for x in range(rimx,w-rimx)]
    ring += [array[y][w-1-rimx] for y in range(rimy+1,h-rimy)]
    ring += [array[h-1-rimy][x] for x in range(w-2-rimx, rimx-1, -1)]
    ring += [array[y][rimx] for y in range(h-2-rimy, rimy, -1)]
    if rimx == max_rings or rimy == max_rings or (max_rings == 1 and (w==2 or h==2)):
        return ring
    else:
        return ring + spiral_transposition(array, rimx+1, rimy+1)

