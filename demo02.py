for i in range (1, 10):
    for j in range (1, 10):
        print (f' {i * j:5d}', end = '')
    print ()

print ('- -'* 10)

i = 1
while i < 10:
    j = 1
    while j < 10:
        print (f' {i * j:5d}', end = '')
        j += 1
    print ()
    i += 1

print ('- -'* 10)

n,m = map(int, input('enter two NUMBERs (n m): ').split())

i = 1
while i <= n:
    j = 1
    while j <= m:
        print (f' {i * j:5d}', end = '')
        j += 1
    print ()
    i += 1

print ('- -'* 10)

n,m = map(int, input('enter two NUMBERs (n m): ').split())
i = 1
while i <= n:
    j = 1
    while j <= m:
        print (f' {j **i :5d}', end = '')
        j += 1
    print ()
    i += 1

print ('- -'* 10)

n,m = map(int, input('enter two NUMBERs (n m): ').split())
i = 1
while i <= n:
    j = 1
    while j <= m:
        if i * j >= 50:
            continue
        else :
            print (f' {i * j:5d}', end = '')
        j += 1
    print ()
    i += 1