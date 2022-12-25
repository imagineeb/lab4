def comb(a):
    comb_tooth = len(a) - 1
    while comb_tooth > 0:
        for i in range(0, len(a) - comb_tooth):
            if (a[i] > a[i + comb_tooth]):
                a[i], a[i + comb_tooth] = a[i + comb_tooth], a[i]
        comb_tooth = int(comb_tooth//1.25)
    return a
