
def coloured_triangle(colors):
    if len(colors) == 1:
        return colors
    else:
        return coloured_triangle(
            "".join(RGB[a + b] for a, b in zip(colors, colors[1:]))
        )
    
RGB = {
    "RR": "R",
    "GG": "G",
    "BB": "B",
    "RG": "B",
    "GR": "B",
    "GB": "R",
    "BG": "R",
    "RB": "G",
    "BR": "G",
}

