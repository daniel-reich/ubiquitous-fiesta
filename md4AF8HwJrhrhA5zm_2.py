
def colour_harmony(anchor, combination):
    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    if anchor not in colours:
        return "Anchor not found"
    idx=[]
    x=colours.index(anchor)
    if combination == "complementary":
        idx=[x,x+6]
    elif combination == "analogous":
        idx=[x,x-1,x+1]
    elif combination == "triadic":
        idx=[x,x+4,x-4]
    elif combination == "split_complementary":
        idx=[x,x-5,x+5]
    elif combination == "rectangle":
        idx=[x,x+2,x-4,x+6]
    elif combination == "square":
        idx=[x,x-3,x+3,x+6]
    harmony=[]    
    for i in idx:
        harmony.append(colours[i % len(colours)])
    
    return set(harmony)

