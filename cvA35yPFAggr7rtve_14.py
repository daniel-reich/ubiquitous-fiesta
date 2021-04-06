
def last_ancestor(f, X, Y):
    def iit(f, X):
        switch, main, Z = True, [X], X
        while switch:
            switch = False
            for k, v in f.items():
                if X in v:
                    main.append(k)
                    X = k
                    switch = True
        return main
    return [x for x in iit(f, X) if x in iit(f, Y)][0]

