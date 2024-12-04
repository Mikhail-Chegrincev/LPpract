def f():
    for x in (1,0):
        if not (k := int(input('Ввод: '))):
            return
        if x:
            print('Вывод:', k)
    f()
f()