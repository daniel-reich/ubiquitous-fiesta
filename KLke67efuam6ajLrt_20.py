
def shuffle_count(num):
    main_list = [x for x in range(1, num + 1)]
    split1 = main_list[:len(main_list) // 2]
    split2 = main_list[len(main_list) // 2:]
    shuf_list = []
    count = 0
    while shuf_list != main_list:
        shuf_list = []
        for i in range(len(split1)):
            shuf_list.append(split1.pop(0))
            shuf_list.append((split2.pop(0)))
        print(shuf_list)
        split1 = shuf_list[:len(main_list) // 2]
        split2 = shuf_list[len(main_list) // 2:]
        count += 1
    return count

