
def cc_str_to_hex(s):
    s = s.replace('#', '')
    if len(s) != 6:
        return "Invalid input!"
    try:
        return {'r': int("0x" + s[:2], 16), 'g': int("0x" + s[2:4], 16), 'b': int("0x" + s[4:], 16)}
    except:
        return "Invalid input!"
    
def cc_hex_to_str(h):
    if min(h.values()) < 0 or max(h.values()) > 255:
        return "Invalid input!"
    return '#' + hex(h['r'])[2:].zfill(2) + hex(h['g'])[2:].zfill(2) + hex(h['b'])[2:].zfill(2)
​
def color_conversion(h):
    return cc_str_to_hex(h) if type(h) == str else cc_hex_to_str(h)

