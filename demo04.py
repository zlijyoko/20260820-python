total = 0
while True:
    while True:
        c = int(input ('請輸入 number (輸入 999 停止): '))
        if c == 999:
            break
        total += c
    print(f'Total: {total}')