import random
import time

hp = 100
tg = 12
dmg = 3

oruzie = ["палка", "ржавый мечь", "арматура", "меч", "эскалибур"]
oruzie_playr = []
shop_hp = [2, 3, 4, 5, 6, 7, 8, 9, 10]



def parametrs():
    print(f"У вас {hp} хп, {tg} тенге. {dmg} урона")
    print(f"Ваше оружие: {oruzie_playr}\n")



def shop():
    global dmg
    global tg
    global hp
    sut2 = random.randint(1, 2)
    rsut = random.randint(0, 4)
    rhp = random.randint(0, 8)
    ind = oruzie[rsut]
    ind2 = shop_hp[rhp]
    if sut2 == 1:
        print(f"В магазине продаётся оружие: {ind}, {oruzie.index(ind)} урона, цена: {oruzie.index(ind)} тенге")
        if tg >= oruzie.index(ind):
            wopros = input(f'У вас на счету {tg} тенге, вы можете себе это позволить, купить д/н ')
            if wopros == "д":
                tg -= oruzie.index(ind)
                dmg = dmg + oruzie.index(ind)
                oruzie_playr.append(ind)
                print(f"Вы купили {ind}")
            else:
                pass
        else:
            print(f"У вас на счету всего {tg}, вы не можете себе это позволить")
    elif sut2 == 2:
        print(f"В магазине продаётся {ind2} hp, у вас {hp} hp, и {tg} тенге, цена: {ind2} тенге")
        if tg >= ind2:
            wopros = input(f'У вас на счету {tg} тенге, вы можете себе это позволить, купить д/н ')
            if wopros == "д":
                tg -= ind2
                hp += ind2
                print(f"Вы купили {ind2} hp")
        else:
            print(f"У вас на счету всего {tg}, вы не можете себе это позволить")



def dmgork():
    d = random.randint(1, 4)
    return d


def drdmg():
    d = random.randint(5, 15)
    return d



def ork():
    global hp
    global tg
    global dmg

    hpork = random.randint(1, 6)
    rrun = random.randint(1, 5)

    w = input(f'Попытаться сбежать[н]. Вступить в бой[д]. У орка {hpork} hp ')

    if w == "н":
        print(f'Вы убежали, орк ударил вас нанеся {3} урона')
        hp -= 3
    else:
        while hpork >= 1:
            print("Ударить орка[1]")
            print("Маневрировать удар[2]")
            wу = input()
            if wу == '1':
                hpork -= dmg
                print(f'Вы ударили орка, нанося ему {dmg} урона')
                bee = dmgork()
                print(f"У орка осталось {hpork} хп")
                hp -= bee
                print(f"Орк ударил вас нанося вам {bee} урона, у вас осталось {hp} хп")
            else:
                rrr = dmgork()
                if rrr < 3:
                    print("Вы успешно увернулись от удара орка")
                else:
                    gegeg = dmgork()
                    hp -= gegeg
                    print(f"Увернутся не получилось, орк нанёс вам {gegeg} урона\n у вас осталось {hp} hp")

        print(f"Вы убили орка, с орка выпало {1} тенге")
        tg += 1




def nachalo(attHp, attTg, attDmg):
    global hp
    global tg
    global dmg

    hp = attHp
    tg = attTg
    dmg = attDmg

    print("Если вы умрёте, всё ваше оружие сохранится, но урон нет\nПроцесс в игре не сохраняется\n\n\nВы очнулись в тёмном лесу.\nВсё что вы помните - это то как спокойно пили чашку кофе\n")
    wopros = input('Вы видите свет вдалеке леса, желаете ли вы пойти на свет? д/н\n')
    if wopros == 'д':
        wopros = input("Вы идёте на свет, как вдруг услышали шорох в кустах\n  Игнорировать шум и идти дальше на свет в лесу[1]\n  Проверить[2]\n  Ускортся[3]\n")
        if wopros == '1':
            wopros = input('Вы решили не обращять на шум внимание и пошли дальше на свет\nВы дошли до света, это оказался торговец\nТорговец оказался вполне адыкватным человеком и предложил вам чашечку чая\n  Отпить чая[1]\n  Отказатся[2]\n')
            if wopros == '1':
                wopros = input('Пока вы разговариволи с торговцем, в лесу посветлело\nТорговец дал вам 1 тенге\nВы отправились дальше в лес\n')
                tg += 1
            else:
                print("Торговец разозлился на вас, от злости он превратился в орка")
                ork()
        elif wopros == "2":
            print('В кустах не кого не оказалось, вы зацепились об ядовитую колючку, -1 hp')
            hp -= 1
            wopros = input('Вы пошли дальше на свет\nВы дошли до света, это оказался торговец\nТорговец оказался вполне адыкватным человеком и предложил вам чашечку чая\n  Отпить чая[1]\n  Отказатся[2]\n')
            if wopros == '1':
                wopros = input(
                    'Пока вы разговариволи с торговцем, в лесу посветлело\nТорговец дал вам 1 тенге\nВы отправились дальше в лес\n')
                tg += 1
            else:
                print("Торговец разозлился на вас, от злости он превратился в орка")
                ork()
        elif wopros == "3":
            wopros = input('Вы ускоренно пошли дальше на свет\nВы дошли до света, это оказался торговец\nТорговец оказался вполне адыкватным человеком и предложил вам чашечку чая\n  Отпить чая[1]\n  Отказатся[2]\n')
            if wopros == '1':
                wopros = input(
                    'Пока вы разговариволи с торговцем, в лесу посветлело\nТорговец дал вам 1 тенге\nВы отправились дальше в лес\n')
                tg += 1
            else:
                print("Торговец разозлился на вас, от злости он превратился в орка")
                ork()
    else:
        wopros = input('Вы пошли в кромешную тьму\nВы шли по лесу пока не посветлело пару раз задев ядовитые колючки -7 hp')
        hp -= 7

    parametrs()



def boss():
    global hp
    global dmg
    draghp = 500
    dragdmg = drdmg()

    print(f'Вы зашли в пещеру, как вдруг вас сбило с ног огромным хвостом, -5 hp\nУ вас осталось {hp}')
    hp -= 5
    print('Как только вы очухались от удара, увидели перед собой огромного дракона с 500 hp')

    while draghp >= 1:
        print("Ударить дракона[1]")
        print("Маневрировать удар[2]")
        wу = input()
        if wу == '1':
            draghp -= dmg
            print(f'Вы ударили дакона, нанося ему {dmg} урона')
            bee = drdmg()
            print(f"У дракона осталось {draghp} хп")
            hp -= bee
            print(f"Дракон ударил вас нанося вам {bee} урона, у вас осталось {hp} хп")
        else:
            rrr = dmgork()
            if rrr < 3:
                print("Вы успешно увернулись от удара дракона")
            else:
                gegeg = dmgork()
                hp -= gegeg
                print(f"Увернутся не получилось, дракон нанёс вам {gegeg} урона\n у вас осталось {hp} hp")
    print("\nДракон убит, игра пройдена\nЯ вручаю вам \"Гвардейский вымпел\"\nЧесть ведь важнее денег?")


def loop():
    global tg
    sut = random.randint(1, 100)
    if sut <= 10:
        print("Вы дошли до магазина")
        shop()
    elif sut > 10 and sut < 20:
        print("На вас напал орк!")
        ork()
    elif sut == 22 and sut == 23 and sut == 24 and sut == 26 and sut == 27:
        print("На тропинке вы нашли 1 тенге")
        tg += 1
    elif sut == 31 and sut == 28 and sut == 29:
        wopros = input("Вы дошли до пещеры с боссом, хотители вы с ним сразиться?\n  Да[д]\n  Нет[н]\n")
        if wopros == 'д':
            wopros = input('Оно вам надо?\n  Да[д]\n  Нет[н]\n')
            if wopros == 'д':
                boss()
                wopros = input('Выйти? д/н')
                if wopros == "д":
                    exit()
                else:
                    print("Игра пройдена, если вы читаете это - спасибо вам большое за то что уделили время этой игре(:")
                    input("Введите любой символ чтобы выйти")
                    exit()
            else:
                print('Ну и правильно')
        else:
            print("Вы прошли мимо пещеры с финальным боссом, встретится ли он вам ещё раз?")
    else:
        print("Блуждать...")



nachalo(10, 0, 1)
time.sleep(2)

while True:

    loop()

    if hp <= 0:
        print("Вас убили, хотите начать заново? да/нет")
        fefe = input()
        if fefe == "да":
            nachalo(10, 2, 1)
        else:
            break
    #time.sleep(2)
    wopros = input("Следуйщий ход? д/н. Посмотреть инвентарь [ин]\n")

    if wopros == "ин":
        parametrs()
    else:
        pass