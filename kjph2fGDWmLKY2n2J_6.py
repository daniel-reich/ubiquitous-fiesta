
def valid_color (color):
    def rgb(a,b,c):
        return all(0 <= p <= 255 for p in (a,b,c))
    def rgba(r,g,b,a):
        return rgb(r,g,b) and 0 <= a <= 1
    try: 
        nospace = 'rgb(' in color or 'rgba(' in color
        return nospace and eval(color.replace('%','*2.55'))
    except (SyntaxError, TypeError): return False

