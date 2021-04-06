
def pyramidal_string(string, _type):
    is_inverted = _type == "REV"
    return build_pyramid(string, is_inverted)
​
def build_pyramid(string, is_inverted):
    return build_pyramid_recursive([], list(string), 1, is_inverted)
​
def build_pyramid_recursive(pyramid, blocks, height, is_inverted):
    does_not_have_blocks = len(blocks) == 0
    if (does_not_have_blocks):
        return pyramid
    
    if (is_inverted):
        pyramid_top = blocks[-height:]
        rest_of_blocks = blocks[:-height]
        pyramid = [' '.join(pyramid_top)] + pyramid
        pyramid_top_is_different_from_height = height != len(pyramid_top)
        if (pyramid_top_is_different_from_height):
            return "Error!"
    else:
        pyramid_base = blocks[:height]
        rest_of_blocks = blocks[height:]
        pyramid = pyramid + [' '.join(pyramid_base)]
        pyramid_base_is_different_from_height = height != len(pyramid_base)
        if (pyramid_base_is_different_from_height):
            return "Error!"
​
    return build_pyramid_recursive(pyramid, rest_of_blocks, height + 1, is_inverted)

