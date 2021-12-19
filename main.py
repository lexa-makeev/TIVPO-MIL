import json
import pytest
from tkinter import *

class MainClass:
    start = True
    answer = ''
    data_list = {}

    def __init__(self):
        json_dict = get_data_from_json('dump.json')
        self.data_list = json_dict['data']
        self.count = 0

    def set_count(self, c):
        self.count = c

    def get_count(self):
        return self.count

    def add_count(self):
        self.count += 1

    def get_dict(self):
        return self.data_list

    def set_dict(self, d):
        self.data_list = d

    def print_dict(self):
        print(self.data_list)

    def is_start(self):
        return self.start

    def set_start(self, b):
        self.start = b



# Функция получения данных из json-файла
def get_data_from_json(filename):
    with open(filename, 'r', encoding="utf-8") as file:
        data = file.read()
    return json.loads(data)


class WindowClass:
    def __init__(self, win):
        self.window = win
        self.lbl_value = Label(master=self.window, text="Нажмите на любую кнопку, чтобы начать!", font=("Arial", 12))
        self.btn_a = Button(master=self.window, text="A", command=pressed_a, width=25)
        self.btn_b = Button(master=self.window, text="B", command=pressed_b, width=25)
        self.btn_c = Button(master=self.window, text="C", command=pressed_c, width=25)
        self.btn_d = Button(master=self.window, text="D", command=pressed_d, width=25)

        lbl_value_1 = Label(master=self.window, text="500", font=("Arial", 20))
        lbl_value_2 = Label(master=self.window, text="1000", font=("Arial", 20))
        lbl_value_3 = Label(master=self.window, text="2000", font=("Arial", 20))
        lbl_value_4 = Label(master=self.window, text="3000", font=("Arial", 20))
        lbl_value_5 = Label(master=self.window, text="5000", font=("Arial", 20))
        lbl_value_6 = Label(master=self.window, text="10000", font=("Arial", 20))
        lbl_value_7 = Label(master=self.window, text="15000", font=("Arial", 20))
        lbl_value_8 = Label(master=self.window, text="25000", font=("Arial", 20))
        lbl_value_9 = Label(master=self.window, text="50000", font=("Arial", 20))
        lbl_value_10 = Label(master=self.window, text="100000", font=("Arial", 20))
        lbl_value_11 = Label(master=self.window, text="200000", font=("Arial", 20))
        lbl_value_12 = Label(master=self.window, text="400000", font=("Arial", 20))
        lbl_value_13 = Label(master=self.window, text="800000", font=("Arial", 20))
        lbl_value_14 = Label(master=self.window, text="1500000", font=("Arial", 20))
        lbl_value_15 = Label(master=self.window, text="3000000", font=("Arial", 20))

        self.lbl_value.place(x=100, y=400)
        self.btn_a.place(x=100, y=450)
        self.btn_b.place(x=320, y=450)
        self.btn_c.place(x=100, y=500)
        self.btn_d.place(x=320, y=500)

        lbl_value_1.place(x=550, y=430)
        lbl_value_2.place(x=535, y=400)
        lbl_value_3.place(x=535, y=370)
        lbl_value_4.place(x=535, y=340)
        lbl_value_5.place(x=535, y=310)
        lbl_value_6.place(x=520, y=280)
        lbl_value_7.place(x=520, y=250)
        lbl_value_8.place(x=520, y=220)
        lbl_value_9.place(x=520, y=190)
        lbl_value_10.place(x=505, y=160)
        lbl_value_11.place(x=505, y=130)
        lbl_value_12.place(x=505, y=100)
        lbl_value_13.place(x=505, y=70)
        lbl_value_14.place(x=490, y=40)
        lbl_value_15.place(x=490, y=10)

        self.lbl_arr = [lbl_value_1, lbl_value_2, lbl_value_3, lbl_value_4, lbl_value_5,
                        lbl_value_6, lbl_value_7, lbl_value_8, lbl_value_9, lbl_value_10,
                        lbl_value_11, lbl_value_12, lbl_value_13, lbl_value_14, lbl_value_15]

    def set_score(self, count):
        if count < 16:
            self.lbl_arr[count].config(bg='orange')
        if 0 < count < 15:
            self.lbl_arr[count - 1].config(bg='green')

    def update_ask(self, dictionary, i):
        print("Update: " + str(i))
        for element in dictionary:
            if element["id"] == i:
                self.lbl_value.config(text="" + element["ask"])
                self.btn_a.config(text="A: " + element["answerA"])
                self.btn_b.config(text="B: " + element["answerB"])
                self.btn_c.config(text="C: " + element["answerC"])
                self.btn_d.config(text="D: " + element["answerD"])
                self.btn_a.update()
                self.btn_b.update()
                self.btn_c.update()
                self.btn_d.update()


def next_ask(main, win):
    c = main.get_count()
    if c < 15:
        main.add_count()
        win.set_score(c)
    else:
        next_game(main, win)


def next_game(main, win):
    main.set_count(0)
    main.set_start(True)
    for i in range(len(win.lbl_arr)):
        win.lbl_arr[i].config(bg='white')
        win.lbl_arr[i].update()
    win.btn_a.config(text="A: ")
    win.btn_b.config(text="B: ")
    win.btn_c.config(text="C: ")
    win.btn_d.config(text="D: ")
    win.btn_a.update()
    win.btn_b.update()
    win.btn_c.update()
    win.btn_d.update()
    win.lbl_value.config(text="Нажмите на любую кнопку, чтобы начать!")
    win.lbl_value.update()


def pressed_a():
    if m.is_start():
        m.set_start(False)
        w.update_ask(m.get_dict(), 1)
        next_ask(m, w)
    else:
        pressed_letter = 'a'
        d = m.get_dict()
        for element in d:
            if element["id"] == m.get_count():
                if element["answer"] == pressed_letter:
                    next_ask(m, w)
                    w.update_ask(m.get_dict(), m.get_count())
                    break
                else:
                    next_game(m, w)


def pressed_b():
    if m.is_start():
        m.set_start(False)
        w.update_ask(m.get_dict(), 1)
        next_ask(m, w)
    else:
        pressed_letter = 'b'
        d = m.get_dict()
        for element in d:
            if element["id"] == m.get_count():
                if element["answer"] == pressed_letter:
                    next_ask(m, w)
                    w.update_ask(m.get_dict(), m.get_count())
                    break
                else:
                    next_game(m, w)


def pressed_c():
    if m.is_start():
        m.set_start(False)
        w.update_ask(m.get_dict(), 1)
        next_ask(m, w)
    else:
        pressed_letter = 'c'
        d = m.get_dict()
        for element in d:
            if element["id"] == m.get_count():
                if element["answer"] == pressed_letter:
                    next_ask(m, w)
                    w.update_ask(m.get_dict(), m.get_count())
                    break
                else:
                    next_game(m, w)


def pressed_d():
    if m.is_start():
        m.set_start(False)
        w.update_ask(m.get_dict(), 1)
        next_ask(m, w)
    else:
        pressed_letter = 'd'
        d = m.get_dict()
        for element in d:
            if element["id"] == m.get_count():
                if element["answer"] == pressed_letter:
                    next_ask(m, w)
                    w.update_ask(m.get_dict(), m.get_count())
                    break
                else:
                    next_game(m, w)


# Главная функция
if __name__ == '__main__':
    window = Tk()  # Объявление окна
    window.title("Игра")  # Задание имени окна
    window.geometry('620x550')  # Задание размера окна
    window.config(bg='black')

    img = PhotoImage(file="image.gif")
    labelPhoto = Label(master=window, image=img)
    labelPhoto.place(x=-30, y=0)

    m = MainClass()  # Главный объект
    w = WindowClass(window)  # Объект окна
    w.window.mainloop()  # Запуск окна
