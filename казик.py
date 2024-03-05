import random
import time
du = True
d = True
dud = True
krutka = 0
chislo = 0
zvet = ''
stavka1 = ''
end_zvet = ''
while d:
    print("КАЗИНО ВУЛКАН, СТАВКИ НА РУЛЕТКУ")
    print("Если хотите поставить на зону, введите 1. Если хотите поставить на цвет, введите 2. Если хотите поставить на цифру, введите 3. Если хотите закончить, введите СТОП")
    a = input()
    while du:
        if a == '1' or a == '2' or a == '3' or a.lower() == 'стоп':
            du = False
            continue
        print("КАЗИНО ВУЛКАН, СТАВКИ НА РУЛЕТКУ")
        print("Если хотите поставить на зону, введите 1. Если хотите поставить на цвет, введите 2. Если хотите поставить на цифру, введите 3. Если хотите закончить, введите СТОП")
        a = input()

    if a.lower() == 'стоп':     #остановка программы
        d = False
        continue

    if a == '1':                                      # выбор зоны
        print("Зоны на которые можно поставить: ")
        print("Voinsins de zero (17 цифр - 22,18,29,7,28,12,35,3,26,0,32,15,19,4,21,2,25")
        print("Orphelins (8 цифр - 9,31,14,20,1,17,34,6")
        print("Tier (12 цифр - 27,13,36,11,30,8,23,10,5,24,16,33")
        stavka1 = input("Введите название ставки - ")
        if stavka1.lower() != 'voinsins de zero' and stavka1.lower() != 'orphelins' and stavka1.lower() != 'tier':
            while dud: # цикл для верного ввода
                print("Вы ввели неверное значение, напишите название зоны")
                stavka1 = input("Введите название ставки - ")
                if stavka1.lower() == 'voinsins de zero' or stavka1.lower() == 'orphelins' or stavka1.lower() == 'tier':
                    stavka1 = stavka1.lower()
                    dud = False
                    continue
    if a == '2':
        print("Введите цвет на который хотите поставить (красный,чёрный,зеленый) - ")
        zvet = input()
        while zvet.lower() != 'красный' and zvet.lower() != 'чёрный' and zvet.lower() != 'зеленый':
            print("Неправильно введён цвет. Попробуйте ещё раз")
            zvet = input("Введите цвет на который хотите поставить (красный,чёрный,зеленый) - ")
            if zvet.lower() == 'красный' and zvet.lower() == 'чёрный' and zvet.lower() == 'зеленый':
                zvet = zvet.lower()
                continue

    if a == '3':
        print("Введите число от 0 до 36")
        chislo = int(input())

        while chislo > 36 or chislo < 0:
            print("Введите число от 0 до 36")
            chislo = int(input())

    krutka = random.randint(0,36)
    for i in range(random.randint(2,5)):
        print("Идет крутка колеса",end='')
        time.sleep(0.5)
        print(".",end='')
        time.sleep(0.5)
        print(".", end='')
        time.sleep(0.5)
        print(".", end='')
        print(end="\n")
        time.sleep(1.5)

    if a == '1':
        time.sleep(1)
        print("Вы выбрали ставку на зону", stavka1,end='\n')
        time.sleep(0.5)
        print("Выпавшее число", krutka,end='  ')
        if krutka == 22 or krutka == 18  or krutka == 29 or krutka == 7 or krutka == 28 or krutka == 12 or krutka == 35 or krutka == 3 or krutka == 26 or krutka == 0 or krutka == 32 or krutka == 15 or krutka == 19 or krutka == 4 or krutka == 21 or krutka == 2 or krutka == 25:
            time.sleep(0.5)
            print('Данное число относиться к зоне "Voinsins de zero" ')
        elif krutka == 9 or krutka == 31 or krutka == 14 or krutka == 20 or krutka == 1 or krutka == 17 or krutka == 34 or krutka == 6:
            time.sleep(0.5)
            print('Данное число относиться к зоне "Orphelins" ')
        else:
            time.sleep(0.5)
            print('Данное число относиться к зоне "Tier" ')

        if (krutka == 22 or krutka == 18  or krutka == 29 or krutka == 7 or krutka == 28 or krutka == 12 or krutka == 35 or krutka == 3 or krutka == 26 or krutka == 0 or krutka == 32 or krutka == 15 or krutka == 19 or krutka == 4 or krutka == 21 or krutka == 2 or krutka == 25) and stavka1.lower() == 'voinsins de zero':
            print("ВЫ ВЫИГРАЛИ!")
        elif (krutka == 9 or krutka == 31 or krutka == 14 or krutka == 20 or krutka == 1 or krutka == 17 or krutka == 34 or krutka == 6) and stavka1.lower() == 'orphelins':
            print("ВЫ ВЫИГРАЛИ!")
        elif (krutka == 27 or krutka == 13 or krutka == 36 or krutka == 11 or krutka == 30 or krutka == 8 or krutka == 23 or krutka == 10 or krutka == 5 or krutka == 24 or krutka == 16 or krutka == 33) and stavka1.lower() == 'tier':
            print("ВЫ ВЫИГРАЛИ!")
        else:
            print("ВЫ ПРОИГРАЛИ!")
            time.sleep(4)
            print(":(")
            time.sleep(0.5)
            print(":(")
            time.sleep(0.5)
            print(":(")
        print(end="\n")
        print(end="\n")

    if a == '2':
        time.sleep(1)
        print("Вы выбрали ставку на цвет - ", zvet, end='\n')
        time.sleep(0.5)
        print("Выпавший цвет -", end=' ')
        if krutka == 0:
            print("зеленый")
            end_zvet = 'зелный'
        elif krutka == 3 or krutka == 32  or krutka == 19  or krutka == 21  or krutka == 25  or krutka == 34  or krutka ==  27  or krutka == 36  or krutka == 30  or krutka == 23  or krutka == 5  or krutka == 16  or krutka == 1  or krutka == 14  or krutka == 9  or krutka == 18  or krutka == 7  or krutka == 12:
            print('красный')
            end_zvet = 'красный'
        else:
            print('черный')
            end_zvet = 'черный'
        if zvet.lower() == end_zvet:
            time.sleep(3)
            print("ВЫ ВЫИГРАЛИ!")
        else:
            print("ВЫ ПРОИГРАЛИ!")
            time.sleep(4)
            print(":(")
            time.sleep(0.5)
            print(":(")
            time.sleep(0.5)
            print(":(")
        print(end="\n")
        print(end="\n")

    if a == '3':
        time.sleep(1)
        print("Вы выбрали ставку на число - ", chislo, end='\n')
        time.sleep(0.5)
        print("Выпавшее число - ",krutka, end='\n')
        if int(krutka) == int(chislo):
            print("ВЫ ВЫИГРАЛИ!")
        else:
            print("ВЫ ПРОИГРАЛИ!")
    time.sleep(5)