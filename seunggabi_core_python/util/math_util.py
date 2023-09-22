def safe_divide(x, y):
    return x / y if y else 0


def safe_range(x, _min, _max):
    return max(min(x, _max), _min)
