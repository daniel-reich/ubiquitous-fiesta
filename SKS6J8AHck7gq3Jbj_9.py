
def tidy_books(lst):
    final_book_list = []
    for book_info in lst:
        for var in book_info:
            var = var.rstrip().lstrip()
            new_book_info = var.split('-')
            new_book_info[0], new_book_info[1] = new_book_info[0].rstrip(), new_book_info[1].lstrip()
            final_book_list.append(new_book_info)
    return final_book_list

