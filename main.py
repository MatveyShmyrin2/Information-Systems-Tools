import pymysql


# Задача 1
def t1():
    myString = input("Введите строку: ")
    myString = myString.replace(" ", "")
    for i in range(len(myString)):
        if myString[i].upper() != myString[-(i + 1)].upper():
            print("Нет")
            return
    print("Да")


# Задача 2
def t2():
    a = []
    while True:
        newInput = input().split()
        if newInput == ["end"]:
            break
        else:
            a.append(newInput)
    for i in a:
        print(min(i))


# Задача 3
def t3():
    names = input().lower().split()
    unique_numbers = list(set(names))
    d = dict.fromkeys(unique_numbers)
    for i in range(len(names)):
        d[names[i]] = 0
    for i in range(len(names)):
        d[names[i]] += 1
    for i in range(len(unique_numbers)):
        print(str(i + 1) + ' ) ' + unique_numbers[i] + ' : ' + str(d[unique_numbers[i]]))


def t4():
    connect = pymysql.connect(host="127.0.0.1", user="root", password="pass", db="my_db")
    sql = "select first_name, last_name, date_of_birth from user where year(date_of_birth) = %s"
    year = input("Введите год: ")
    cur = connect.cursor()
    cur.execute(sql, year)
    for rec in cur:
        print(rec[0], rec[1], rec[2])


t1()

t2()

t3()

t4()
# Введите год: 1984
# Garry Fancie 1984-08-11
# Chastity Hettie 1984-06-03
# Yvet Ertan 1984-12-02
