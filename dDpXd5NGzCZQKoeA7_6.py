
def num_args(func):
    try:
        function = func()
        return 0
    except Exception as err:
        return int(str(err)[19:21])

