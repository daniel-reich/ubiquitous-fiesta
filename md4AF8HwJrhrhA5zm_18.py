
def colour_harmony(anchor, combination):
    colours = ["red", "red-orange", "orange", "yellow-orange",
               "yellow", "yellow-green",  "green", "blue-green",
               "blue", "blue-violet", "violet", "red-violet"]
    d = {'complementary':[6],
         'analogous':[1,11],
         'triadic':[4,8],
         'split_complementary':[5,7],
         'rectangle':[2,6,8],
         'square':[3,6,9]}
    combs = d[combination]
    start = colours.index(anchor)
    ans = {anchor}
    for c in combs:
        idx = (c + start) % 12
        ans.add(colours[idx])
    return ans

