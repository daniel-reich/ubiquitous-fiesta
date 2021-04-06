
def colour_harmony(anchor, combination):
    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    anchor_offsets = {'complementary': [0,-6], 'analogous': [0,-1,1], 'triadic':[0,-4,4], 'split_complementary':[0,-5,5], 'rectangle':[0,-6,-4,2], 'square':[0,-6,-3,3]}
    return {colours[(colours.index(anchor)+idx)%len(colours)] for idx in anchor_offsets[combination]}

