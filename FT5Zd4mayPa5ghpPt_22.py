
from PIL import ImageColor
​
def clamp(x):
    return max(0, min(x, 255))
​
def color_conversion(h):
    """[Color Conversion] RGB to HEX and HEX to RGB"""
    if isinstance(h, dict):
        r, g, b = h["r"], h["g"], h["b"]
        
        for c in [r, g, b]:
            if c > 255 or c < 0:
                return "Invalid input!"
        
        return "#{:02x}{:02x}{:02x}".format(r, g, b)
    else:
        try:
            if h.count("#") == 0:
                h = "#" + h
            r, g, b = ImageColor.getcolor(h, "RGB")[:]
            return {"r": r, "g": g, "b": b}
        except:
            return "Invalid input!"

