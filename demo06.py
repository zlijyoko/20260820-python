import demo05

def main ():
    students = [
        {'name': "yoko", 'age': 20, 'gender': 'female'},
        {'name': "nana", 'age': 21, 'gender': 'female'}
    ]
    print (students[1], students[1]['name'], students[1]['age'], students[1]['gender'])
    print (students[0], students[0]['name'], students[0]['age'], students[0]['gender'])


if __name__ == '__main__':
    main()
    while True:
        demo05.showmenu()
        choice = input ('enter your choice (1-4, q to quit): ')
        if choice == '1':
            demo05.showinfo()
        elif choice == '2':
            n = int(input ('enter a number: '))
            demo05.fun1(n)
        elif choice == '3':
            n = int(input ('enter a number: '))
            x = demo05.fun2(n)
            print (f'{n}! = {x}')
        elif choice == '4':
            c = int(input ('enter temperature in Celsius: '))
            f = demo05.c2f(c)
            print (f'{c}°C = {f}°F')
        elif choice == 'q':
            break
        else:
            print ('Invalid choice. Please try again.')
