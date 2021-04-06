
colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
​
def colour_harmony(anchor, combination):
    a_idx = colours.index(anchor)
    ans = set([anchor])
    if combination == "triadic":
        ans.add(colours[(a_idx - 4) % 12])
        ans.add(colours[(a_idx + 4) % 12])
    elif combination == "complementary":
        ans.add(colours[(a_idx + 6) % 12])
    elif combination == "split_complementary":
        ans.add(colours[(a_idx - 5) % 12])
        ans.add(colours[(a_idx + 5) % 12])
    elif combination == "square":
        ans.add(colours[(a_idx + 3) % 12])
        ans.add(colours[(a_idx + 6) % 12])
        ans.add(colours[(a_idx + 9) % 12])
    elif combination == "analogous":
        ans.add(colours[(a_idx - 1) % 12])
        ans.add(colours[(a_idx + 1) % 12])
    elif combination == "rectangle":
        ans.add(colours[(a_idx + 2) % 12])
        ans.add(colours[(a_idx + 6) % 12])
        ans.add(colours[(a_idx + 8) % 12])
    else:
        assert False, "Unknown combination, you fool!"
    return ans

