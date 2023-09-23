import time
from tkinter import *
from tkinter import messagebox


def t2():
    print('--- Task 2 ---')
    print("Hello World!")


def t3():
    print('--- Task 3 ---')
    a = 3
    print(type(a))
    a = 3.5
    print(type(a))
    a = 'qwerty'
    print(type(a))
    a = True
    print(type(a))
    a = '123'
    print(type(a))  # a + 1 = TypeError


def t4():
    print('--- Task 4 ---')
    a = 5.7
    a = int(a)
    print(a)
    b = -5.7
    b = int(b)
    print(b)
    c = 3 ** 39 - int(float(3 ** 39))
    print(c)  # 11


def t5():
    print('--- Task 5 ---')
    name = input('Введите имя: ')
    print('Привет, ' + name + '!')


def t6():
    print('--- Task 6 ---')
    x = int(input('Введите X: '))
    y = int(input('Введите Y: '))
    print('Итого минут: ' + str(2 * (x * 60 + y)))


def t7():
    print('--- Task 7 ---')
    a = False
    b = True
    c = False
    print((not (a or b)) and c)


def t8():
    print('--- Task 8 ---')
    year = int(input('Введите год: '))
    if year < 1900 or year > 3000:
        print('Год не входит в выборку')
        return
    elif year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        print('С днём рождения!')
        return
    else:
        print('Год обычный')


def t9():
    print('--- Task 9 ---')
    a = 1
    while a <= 20:
        if a % 2 == 0:
            print(a, end=' ')
        a += 1
    print('')


def t10():
    print('--- Task 10 ---')
    a = 1
    sum = 0
    while a != 0:
        a = int(input('Введите число: '))
        sum += a
    print('Итого: ' + str(sum))


def t11():
    print('--- Task 11 ---')
    x = int(input('X: '))
    y = int(input('Y: '))
    pieces = 1
    while pieces % x != 0 or pieces % y != 0:
        pieces += 1
    print('Нужно разделить пиццу на: ' + str(pieces))


def t12():
    print('--- Task 12 ---')
    string = ''
    for i in range(0, 20):
        if i % 2 == 0:
            string += str(i) + ' '
    print(string)


def t13():
    print('--- Task 13 ---')
    a, b, c, d = [int(input('Введите значение: ')) for i in range(4)]
    print('', end='\t')
    for j in range(c, d + 1):
        print(j, end='\t')
    print()
    for i in range(a, b + 1):
        print(i, end='\t')
        for j in range(c, d + 1):
            print(i * j, end='\t')
        print()


def t14():
    print('--- Task 14 ---')
    n = int(input('Введите n матрицы: '))
    a = [[0] * n for i in range(n)]
    count = 0
    for i in range(n):
        count += 1
        a[0][i] = count
    j = 0
    i = n - 1
    n -= 1
    while len(a) ** 2 != count:
        for k in range(n):
            j += 1
            count += 1
            a[j][i] = count
        for k in range(n):
            i -= 1
            count += 1
            a[j][i] = count
        for k in range(n - 1):
            j -= 1
            count += 1
            a[j][i] = count
        for k in range(n - 1):
            i += 1
            count += 1
            a[j][i] = count
        n -= 2
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end='\t')
        print()


def t15():
    print('--- Task 15 ---')
    time_now = time.time()
    while True:
        if time.time() - time_now > 3600.0:
            messagebox.showinfo('Useful Python',
                                'Вы долго смотрели в монитор, теперь посмотрите в окно.')
            time_now = time.time()  # Фоновый режим через >pythonw main.py


def t16():
    print('--- Task 16 ---')
    time_now = time.time()
    while True:
        if time.time() - time_now > 5.0:
            def showAgain():
                window.after(5000, showAgain)
                window.destroy()

            def quitButton():
                lbl.configure(quit())

            window = Tk()
            window.title('Useful Python')
            window.geometry('400x250')
            lbl = Label(window, text='Отдыхай', font=('Arial Bold', 10))
            lbl.grid(column=1, row=1)

            btn1 = Button(window, text='ОК', command=showAgain)
            btn2 = Button(window, text='ВЫЙТИ', command=quitButton)

            btn1.grid(column=1, row=2)
            btn2.grid(column=1, row=3)
            window.mainloop()
            time_now = time.time()


t2()
t3()
t4()
t5()
t6()
t7()
t8()
t9()
t10()
t11()
t12()
t13()
t14()
t15()
t16()
