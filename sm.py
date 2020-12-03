import sys
import random

# кто дарит
name_list1 = ["Владимир Иванов",
              "Алёна Родимцева",
              "Керилл Соколов",
              "Полина Никульчак",
              "Александр Мухаметгалеев",
              "Эмиль Биккулов",
              "Илья Фурсов",
              "Андрей Рыжиков",
              "Сергей Бовш",
              "Антон Жданов",
              "Ангелина Калинина",
              "Роман Калякин",
              "Елизавета Баянова",
              "Александр Малков",
              "Римма Абрарова",
              "Павел Алексеев",
              "Оля Фролова",
              "Лилиана Байсланова",
              "Каролина Лян",
              "Лиза Локун",
              'Катерина Коблова',
              "Иван Иванищев",
              "Иван Чабанов"]
# кому дарят
name_list2 = ["Владимир Иванов",
              "Алёна Родимцева",
              "Керилл Соколов",
              "Полина Никульчак",
              "Александр Мухаметгалеев",
              "Эмиль Биккулов",
              "Илья Фурсов",
              "Андрей Рыжиков",
              "Сергей Бовш",
              "Антон Жданов",
              "Ангелина Калинина",
              "Роман Калякин",
              "Елизавета Баянова",
              "Александр Малков",
              "Римма Абрарова",
              "Павел Алексеев",
              "Оля Фролова",
              "Лилиана Байсланова",
              "Каролина Лян",
              "Лиза Локун",
              'Катерина Коблова',
              "Иван Иванищев",
              "Иван Чабанов"]
id_store = [['847154448', "Роман Калякин"],
            ['681309508', "Антон Жданов"],
            ["847993090", "Елизавета Баянова"],
            ["382941071", "Андрей Рыжиков"],
            ["860536416", "Алёна Родимцева"],
            ["1080851888", "Павел Алексеев"],
            ["1315089359", "Илья Фурсов"],
            ["1122438456", "Лилиана Байсланова"],
            ["1168753814", "Сергей Бовш"],
            ["1164395917", "Римма Абрарова"],
            ["885189748", "Владимир Иванов"],
            ["1145739622", "Керилл Соколов"],
            ["1448023971", "Полина Никульчак"],
            ["497993250", "Эмиль Биккулов"],
            ["057028950", "Ангелина Калинина"],
            ["795456093", "Александр Малков"],
            ["1154859794", "Оля Фролова"],
            ["1067945878", "Каролина Лян"],
            ["945990807", "Лиза Локун"],
            ["1284712472", "Катерина Коблова"],
            ["1213750305", "Александр Мухаметгалеев"],
            ["1", "Иванищев"],
            ["1206948771", "Иван Чабанов"]]

id_cont = []


class Game():
    def __init__(self):
        super().__init__()
        self.itog = {}

    def main(self, name):
        # Выбираем, кому будут дарить
        ans = str(random.choice(name_list2))
        # проверяем, является-ли сам санта получателем

        if name == ans:
            while name == ans:
                ans = str(random.choice(name_list2))

        # записываем в словарь имя санты и имя получателя
        self.itog[name] = str(name_list2[name_list2.index(ans)])

        # удаляем получателя, у котороо появился санта
        name_list2.pop(name_list2.index(ans))

        # Записываем в файл имя санты и имя получателя внутри файла
        # f = open(f"{name}.txt", 'w', encoding='utf8')
        # f.write(f"Поздравляю, {name}, тебе выпал: {self.itog[name]}")
        # f.close()

        f = open(f"Ключи.txt", "w", encoding='utf-8')
        for i in self.itog:
            x, y = i, self.itog[i]
            f.write(f"Поздравляю, {x}, тебе выпал: {y}\n")
        f.close()
        # Пусть будет, для тестов удобно
        # print((f"Поздравляю, {name}, тебе выпал(а): {self.itog[name]}"))

    # Функция возвращает текст с произвольным именем, которым представился пользователь, и именем, которое ему выпало.
    # Выпавшее имя удаляяется из списка NotSants
    def sec_main(self, id_sant, name):
        f = open("name_list_23.txt", "r", encoding="utf-8")
        p = open("for_me.txt", "a", encoding='utf-8')
        spisok = []
        for i in f.readlines():
            spisok.append(str(i.replace("\n", "")))

        try:
            ans = str(random.choice(spisok))
        except IndexError:
            p.write(f"Сорян, {name}, но почему-то всех разобрали, обратись к моим разработчикам")
            return (f"Сорян, {name}, но почему-то всех разобрали, обратись к моим разработчикам")
        f.close()
        while int(id_sant) == int(ans):
            ans = int(random.choice(spisok))

        spisok.remove(str(ans))
        f = open("name_list_23.txt", "w", encoding="utf-8")
        for i in spisok:
            f.write(f"{str(i)}\n")
        f.close()

        # self.rep(for_sans)

        self.new_func(id_sant, ans)
        for i in id_store:
            if ans == i[0]:
                ans = i[1]

        # for_sans = []
        # s = open("NotSants.txt", "r", encoding="utf-8")
        #
        # for i in s.readlines():
        #     for_sans.append(s)
        #
        # for i in id_store:
        #     if ans != i[0]:
        #         print("QQQQ")
        #         for_sans.append(f"{i[1]}\n")
        #     else:
        #         print("SSSS")
        # print(for_sans)

        p.write(f"Поздравляю, {name} , тебе выпал(a): {ans}\n")
        p.close()
        return (f"Поздравляю, {name} , тебе выпал(a): {ans}")

    def new_func(self, id_sant, p_id):

        f = open("podarki.txt", "a", encoding="utf-8")
        fag = [int(id_sant), int(p_id)]
        f.write(f"{fag}\n")
        f.close()

    # Функция заполнения файла NotSants, списком, который ты передаёшь в аргументах.
    # Если передать ноль, заполнится нормальным списком имён
    def rep(self, listt):
        f = open("NotSants.txt", "w", encoding='utf-8')
        if listt != 1:
            for i in listt:
                f.write(f"{i}")
        else:
            for i in name_list1:
                f.write(f"{i}\n")
        f.close()

    def chat(message):
        r = open('podarki.txt.')
        k = r.readlines()
        print(k)
        for i in range(len(k)):
            l = k[i][0:-1]
            id_1 = l.replace(",", "")
            id_1 = id_1.replace("'", "")
            id_1 = id_1.replace("[", "")
            id_1 = id_1.replace("]", "")
            idd = id_1.split(" ")
            idd_s = str(idd[0])
            idd_p = str(idd[1])

            print(int(idd_s))
            print(int(idd_p))

        # user_ch = message.text
        # user_id = message.from_user.id

        # if int(user_id) == int(k[-1][0]):
        #     bot.send_message(k[-1][1], message.text[2:])

    def porn(self, id):
        if id in id_store:
            return id_store[id]


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == "__main__":
    ex = Game()
    # Вариант запуска для работы
    # for i in name_list1:
    # ex.main(i)
    print(ex.sec_main("1164395917", "Андрей Рыжиков"))
    # ex.rep(1)
    # ex.chat()

    sys.excepthook = except_hook
