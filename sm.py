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
              'Елизавета Баянова']
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
              "Лиза Локун"]
id_store = {'847154448': "Роман Великий (Калякин)",
            '681309508': "Антоша Прекрасный (Жданов)",
            "847993090": "Елизавета Баянова",
            "": "",
            "": "",
            "": "",
            "": ""
            }


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
    def sec_main(self, name):
        f = open("NotSants.txt", "r", encoding="utf-8")
        p = open("for_me.txt", "w", encoding='utf-8')
        spisok = f.readlines()
        try:
            ans = str(random.choice(spisok))
        except IndexError:
            p.write(f"Сорян, {name}, но почему-то всех разобрали, обратись к моим разработчикам")
            return (f"Сорян, {name}, но почему-то всех разобрали, обратись к моим разработчикам")
        spisok.remove(ans)
        f.close()
        self.rep(spisok)

        p.write(f"Поздравляю, {name} , тебе выпал(a): {ans}\n")
        return (f"Поздравляю, {name} , тебе выпал(a): {ans}")

        # ans = str()

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
    print(ex.porn("847154448"))
    # ex.rep(1)
    # print(ex.sec_main("fdfd"))

    sys.excepthook = except_hook
