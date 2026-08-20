def showinfo ():
    print ('my name is yoko')

def fun1(n):
    for i in range (n + 1):
        for j in range (i):
            print ('*', end = '')
        print ()

def fun2(n):
    res = 1
    for i in range (n, 1, -1):
        res *= i
    return res

def c2f(c):
    return c * 9 / 5 + 32

def showmenu ():
    print ('1. showinfo')
    print ('2. print stars')
    print ('3. Calculate factorial')
    print ('4. Celsius to Fahrenheit')

if __name__ == '__main__':
    showinfo()
    fun1(5)
    x = fun2(5)
    print ('5! =', x)
    c = int(input ('enter temperature in Celsius: '))
    f = c2f(c)
    print (f'{c}°C = {f}°F')
