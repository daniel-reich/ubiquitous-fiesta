
def colour_harmony(anchor, combination):
    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    ans = []
    if combination == "complementary":
        ans.append(anchor)
        ans.append(colours[(colours.index(anchor)+6)%len(colours)])
    elif combination == "analogous":
        ans.append(anchor)
        ans.append(colours[(colours.index(anchor)-1)%len(colours)])
        ans.append(colours[(colours.index(anchor)+1)%len(colours)])
    elif combination == "triadic":
        ans.append(anchor)
        ans.append(colours[(colours.index(anchor)+4)%len(colours)])
        ans.append(colours[(colours.index(anchor)-4)%len(colours)])
    elif combination == "split_complementary":
        ans.append(anchor)
        ans.append(colours[((colours.index(anchor)-5)%len(colours))])
        ans.append(colours[((colours.index(anchor)+5)%len(colours))])
    elif combination == "rectangle" or combination == "tetradic":
        ans.append(anchor)
        ans.append(colours[(colours.index(anchor)+6)%len(colours)]) #complementary
        katabi = (colours.index(anchor)+2)%len(colours)
        ans.append(colours[katabi])
        ans.append(colours[(katabi+6)%len(colours)])
    elif combination == "square":
        ans.append(anchor)
        ans.append(colours[(colours.index(anchor)+6)%len(colours)])
        ans.append(colours[(colours.index(anchor)-3)%len(colours)])
        ans.append(colours[(colours.index(anchor)+3)%len(colours)])
​
​
    return set(ans)

