import random
import time

dif = 0.2
try:
    diff = int(input("Выберите сложность:\n1. Простая\n2. Сложная\n>>> "))
except:
    print("Введите корректный ответ!")
    if diff == 1:
        pass
    else:
        dif = 0.3

lvl = 0
raund = 1
max_raund = 30
roll = 3
hp = 60
attack = 2
bonus = 0
bonus_x = 0
start = time.time()
numbs = [random.randint(1, 5) for _ in range(5)]

while max_raund >= raund and attack > 0:

    x = 0
    x = x + raund + bonus_x

    summa = sum(numbs)
    if summa % 2 == 0:
        x += 2
    elif summa % 3 == 0:
        x += 3
    else:
        pass
    summa += bonus

    print(f"Волна: {raund}/{max_raund}\nОчки: {hp}, вы уменьшите на: {summa * x}\nКол-во перекрутов: {roll}, кол-во атак: {attack}")
    print(numbs)

    try:
        ch = (int(input("1. Перекрутить\n2. Атаковать\n3. Посмотреть множители\n>>> ")))
    except:
        print("Введи корректное число!")

    if ch > 3:
        print("Такого выбора нет!\n\n\n")
    
    if ch == 3:
        print(f"Бонусы:\nДелится на 2: +2, на 3: +3 (к множиелю)\nВаши улучшения:\nДоп.множитель: {x}, доп.очки: {bonus}")

    if ch == 2:
        if attack == 0 and summa * x > hp:
            pass
        elif attack > 0:
            pass
        else:
            attack = -1
        summa *= x
        attack -= 1
        hp -= summa
        numbs = [random.randint(1, 5) for _ in range(5)]
        print("\n\n\n\n\n\n\n\n")

    if ch == 1:
        if roll < 1:
            print("Больше нету попыток!")
            continue
        numbs = [random.randint(1, 5) for _ in range(5)]
        roll -= 1
        print("\n\n\n\n\n\n\n\n")

    if hp <= 0:
        raund += 1
        attack = raund // 10 + 2
        roll = raund // 10 + 3
        if raund <= 10:
            hp = int(100 * ((dif) * raund + 1))
        elif raund <= 20:
            hp = int(100 * ((dif * 2) * raund + 1))
        elif raund >= 25:
            hp = int(100 * ((dif * 4) * raund + 1))

        if raund % 4 == 0:
            while True:
                try:
                    choise = int(input("Выберите бонус:\n1. +3 очков\n2. +0.5 к множителю\n>>> "))
                except:
                    print("Введите верное значение!")
                if choise >= 3:
                    continue
                elif choise == 2:
                    bonus_x += 0.5
                    break
                else:
                    bonus += 3
                    break

if attack <= 0:
    print("Вы проиграли!")
else:    
    elapsed = int(time.time() - start)
    print(f"Понадобилось {elapsed} секунд ({elapsed / 60} минут)")
