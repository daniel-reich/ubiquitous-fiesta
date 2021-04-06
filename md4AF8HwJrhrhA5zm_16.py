
def colour_harmony(anchor,scheme):
    final = []
    colours = ["red", "red-orange", "orange", "yellow-orange", "yellow", "yellow-green",  "green", "blue-green", "blue", "blue-violet", "violet", "red-violet"]
    dictionary = {"complementary": [0,6],
    "analogous": [-1,0,1],
    "triadic": [4,0,-4],
    "split_complementary": [5,0,-5],
    "rectangle": [2,6,8,0],
    "square": [0,3,6,9]
    }
    
    loop = dictionary[scheme]
    
    for item in loop:
        
        anchor_position = colours.index(anchor)
        
        if item == 0:
            final.append(colours[anchor_position])
        
        if item != 0:
            to_append = anchor_position + item
            if to_append > 11:
                final_append = to_append - 12
                final.append(colours[final_append])
            if to_append < 0:
                final_append = 12 + to_append
                final.append(colours[final_append])
                
            if to_append >= 0 and to_append <= 11:
                final.append(colours[to_append])
    return set(final)

