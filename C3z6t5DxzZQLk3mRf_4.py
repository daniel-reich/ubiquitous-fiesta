
def tune(lst, good_freqs = [329.63, 246.94, 196.00, 146.83, 110.00, 82.41]):
    def status_message(ratio):
        if 1.020 < ratio:
            return '>>+'
        elif 1.005 < ratio <= 1.020:
            return '>+'
        elif 0.980 <= ratio < 0.995:
            return '+<'
        elif ratio < 0.980:
            return '+<<'
        else:
            return 'OK'
    return [status_message(good/actual) if actual != 0 else ' - ' for  good,actual in zip(good_freqs, lst)]

