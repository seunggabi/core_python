def unit(n):
    n = abs(n)
    index = str(n).find('.')

    if n < 10:
        decimal = str(n)[index + 1:]
        return 10 ** -len(decimal)
    if n < 100:
        return 0.1

    m = len(str(n))
    v = 10 ** ((m - 3) // 2)

    if m % 2 == 0:
        v *= 5

    return v
