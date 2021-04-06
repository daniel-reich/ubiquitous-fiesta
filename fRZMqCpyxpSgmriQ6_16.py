
def sorting(s):
    from string import ascii_uppercase, ascii_lowercase
    ascii_letters_and_number = "".join(
        [lowe + upper for lowe, upper in zip(ascii_lowercase, ascii_uppercase)]) + "".join(
        [str(item) for item in range(0, 10)])
    source_dict = {item: ascii_letters_and_number.index(item) for item in ascii_letters_and_number}
    result_dict = {source_dict.get(item): item for item in s}
    return "".join([item[1] for item in sorted(result_dict.items())])

