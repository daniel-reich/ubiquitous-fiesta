
def get_frame(w, h, ch):
    result = [[w*ch] if a == 1 or a == h
              else [ch + (w-2)*" " + ch]
              for a in range(1, h+1)]
    return "invalid" if w <= 2 or h <=2 else result

