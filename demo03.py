n, m, k = map(int, input('enter three NUMBERs (n m k): ').split())
for i in range (1, n + 1):
    for j in range (1, m + 1):
        product = i * j
        if product >= k:
            continue
        else :
            print (f' {product:5d}', end = '')
    print ()