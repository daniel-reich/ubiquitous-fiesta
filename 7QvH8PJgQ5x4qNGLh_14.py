
def countdown(n, txt):
    i = n
    end = ""
    for g in range(n):
        end += str(i) + ". "
        i -= 1
    end += txt.upper() + "!"
    return end

