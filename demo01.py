lst = [1,2,3,4,5]

for item in lst:
    print(item)

print ('- -'* 10)

i = 0
while i < len(lst):
    print(lst[i])
    i += 1 

lst = []
"""
讓使用者持續輸入溫度 直到輸入 999 停止 ( 不含 999 ) ，
將輸入的溫度存入 lst 中，最後印出 lst 中所有溫度的平均值。
"""

c = float (input ('請輸入溫度 (輸入 999 停止): '))
while c != 999:
    lst .append(c)
    c = float (input ('請輸入溫度 (輸入 999 停止): '))

print ('平均溫度為: ', sum(lst) / len(lst))


c = float (input ('請輸入 number (輸入 999 停止): '))
total = 0
while c != 999 and c % 2 == 0:
    total += c
    c = int (input ('請輸入 number (輸入 999 停止): '))
print ('total: ', total)