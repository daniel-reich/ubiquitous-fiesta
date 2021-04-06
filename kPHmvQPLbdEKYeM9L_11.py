
def asteroid_collision(asteroids):
    qtd = len(asteroids)
    remain = [asteroids[0]]
    add_ast = remain.append
    rem_ast = remain.pop
    pos = 1
    while pos < qtd:
        ast = asteroids[pos]
        if ast > 0:
            add_ast(ast)
            pos += 1
        else:
            if remain[-1] < 0:
                add_ast(ast)
                pos += 1
            else:
                if remain[-1] < abs(ast):
                    rem_ast()
                    if not remain:
                        add_ast(ast)
                        pos += 1
                elif remain[-1] == abs(ast):
                    rem_ast()
                    pos += 1
                else:
                    pos += 1
    return remain

