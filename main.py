from tkinter import *


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


def pressed_a():
    print("a")


def pressed_b():
    print("b")


def pressed_c():
    print("c")


def pressed_d():
    print("d")


# Главная функция
if __name__ == '__main__':
    window = Tk()  # Объявление окна
    window.title("Игра")  # Задание имени окна
    window.geometry('620x550')  # Задание размера окна
    window.config(bg='black')

    w = WindowClass(window)  # Объект окна
    w.window.mainloop()  # Запуск окна
