
import re
​
symbols = "!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}"
invalid = r"(?:^.{0,5}$)|(?:^.{31,}$)|(?:^.*[\s].*$)|(?:^[^a-z]*$)|(?:^[^A-Z]*$)|(?:^[^\d]*$)|(?:^[^!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}]*$)"
weak = "^(?!(?:^.{0,5}$)|(?:^.{31,}$)|(?:^.*[\s].*$)|(?:^[^a-z]*$)|(?:^[^A-Z]*$)|(?:^[^\d]*$)|(?:^[^!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}]*$))((?:.{6,15})|(?:(?:[^a-z]*[a-z][^a-z]*){1,2})|(?:(?:[^A-Z]*[A-Z][^A-Z]*){1,2})|(?:(?:[^\d]*[\d][^\d]*){1,2})|(?:(?:[^!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}]*[!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}][^!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}]*){1,2}))$"
strong = "^(?!(?:^.{0,15}$)|(?:^.{31,}$)|(?:^.*[\s].*$)|(?:^[^a-z]*$)|(?:^[^A-Z]*$)|(?:^[^\d]*$)|(?:^[^!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}]*$)|^((?:.{6,15})|(?:(?:[^a-z]*[a-z][^a-z]*){1,2})|(?:(?:[^A-Z]*[A-Z][^A-Z]*){1,2})|(?:(?:[^\d]*[\d][^\d]*){1,2})|(?:(?:[^!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}]*[!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}][^!\"#\$%&'\(\)\*\+,-\.\/:;<=>\?@\[\]\^_\\\{\|\}]*){1,2}))$).*$"
