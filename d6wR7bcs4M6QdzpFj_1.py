
def repeat(l, n): l[:] = l * n; return l
def add(l, x): l.append(x); return l
def remove(l, i, j): del l[i:j+1]; return l
def concat(a, b): a.extend(b); return a

