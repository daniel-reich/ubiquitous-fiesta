
import re
​
def color_conversion(h):
    if isinstance(h, str):
        if not re.search(r"^#?[a-f0-9]{6}$", h):
            return "Invalid input!"
        color = ["r", "g", "b"]
        size = len(h)
        if size == 6:
            start = 0
        else:
            start = 1
        value = [int(h[i:i+2], 16) for i in range(start, size, 2)]
        return {c: value[i] for i, c in enumerate(color)}
    red, green, blue = h["r"], h["g"], h["b"]
    if (red < 0 or red > 255) or (green < 0 or green > 255) or (blue < 0 or blue > 255):
        return "Invalid input!"
    return "#" + "".join("0" + hex(ch)[2:] if len(hex(ch)[2:]) == 1 else hex(ch)[2:] for ch in [red, green, blue])

