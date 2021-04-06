
def seq_level(lst):
    
    lst = [lst[i] - lst[i -1] for i in range(1, len(lst))]
    if len(set(lst)) == 1:
        return "Linear"
    lst = [lst[i] - lst[i -1] for i in range(1, len(lst))]
    if len(set(lst)) == 1:
        return "Quadratic"
    lst = [lst[i] - lst[i -1] for i in range(1, len(lst))]
    if len(set(lst)) == 1:
        return "Cubic"

