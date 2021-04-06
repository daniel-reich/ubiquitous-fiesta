
def sort_by_length(lst):
    main=sorted([len(x) for x in lst])
    main2=[b for a in main for b in lst if a==len(b)]
    return main2

