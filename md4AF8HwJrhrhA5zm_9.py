
def colour_harmony(anchor, combination):
    lst = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    pos = lst.index(anchor)
    comp = (pos+len(lst)//2)%len(lst)
    
    if combination == 'complementary':
        return {anchor, lst[comp]}
    if combination == 'split_complementary':
        return {anchor, lst[(comp+1)%len(lst)], lst[(comp-1)%len(lst)]}
    if combination == 'analogous':
        return {anchor, lst[pos+1%len(lst)], lst[pos-1%len(lst)]}
    if combination == 'square':
        return {lst[comp], lst[(comp-3)%len(lst)], lst[(comp+3)%len(lst)], anchor}
    if combination == 'triadic':
        return {anchor, lst[(comp+2)%len(lst)], lst[(comp-2)%len(lst)]}
    if combination == 'rectangle':
        return {lst[comp], lst[(comp+2)%len(lst)], lst[(pos+2)%len(lst)], anchor}

