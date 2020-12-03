TOKEN = '1491365995:AAFQoCH3lwfP_RFZDKVI0Hx8Q5__UFnkbL8'


def pizda(self):
    if id_sant == ans:
        while id_sant == ans:
            ans = str(random.choice(name_list2))

    записываем
    в
    словарь
    имя
    санты
    и
    имя
    получателя
    self.itog[name] = str(name_list2[name_list2.index(ans)])

    удаляем
    получателя, у
    котороо
    появился
    санта
    name_list2.pop(name_list2.index(ans))

    Записываем
    в
    файл
    имя
    санты
    и
    имя
    получателя
    внутри
    файла
    f = open(f"{name}.txt", 'w', encoding='utf8')
    f.write(f"Поздравляю, {name}, тебе выпал: {self.itog[name]}")
    f.close()

    f = open(f"Ключи.txt", "w", encoding='utf-8')
    for i in self.itog:
        x, y = i, self.itog[i]
        # f.write(f"Поздравляю, {x}, тебе выпал: {y}\n")
    f.close()
    Пусть
    будет, для
    тестов
    удобно
    print((f"Поздравляю, {name}, тебе выпал(а): {self.itog[name]}"))