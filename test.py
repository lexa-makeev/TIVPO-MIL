import unittest
from main import WindowClass, next_ask, MainClass, next_game
from main import get_data_from_json


class MyTestCase(unittest.TestCase):
    def test_something(self):
        m = MainClass()
        temp = m.get_count()
        m.add_count()
        self.assertEqual(temp + 1, m.get_count())  # add assertion here

    def test_ask_3_false(self):
        m = MainClass()
        from tkinter import Tk
        window = Tk()  # Объявление окна
        w = WindowClass(window)
        m.set_start(False)
        m.add_count()
        m.add_count()
        m.add_count()
        pressed_letter = 'a'  # Буква нажатой кнопки
        d = m.get_dict()
        for element in d:
            if element["id"] == m.get_count():
                if element["answer"] == pressed_letter:
                    next_ask(m, w)
                    w.update_ask(m.get_dict(), m.get_count())
                    break
                else:
                    next_game(m, w)
        self.assertEqual(m.get_count(), 0)  # add assertion here

    def test_ask_3_true(self):
        m = MainClass()
        from tkinter import Tk
        window = Tk()  # Объявление окна
        w = WindowClass(window)
        m.set_start(False)
        m.add_count()
        m.add_count()
        m.add_count()
        pressed_letter = 'c'  # Буква нажатой кнопки
        d = m.get_dict()
        for element in d:
            if element["id"] == m.get_count():
                if element["answer"] == pressed_letter:
                    next_ask(m, w)
                    w.update_ask(m.get_dict(), m.get_count())
                    break
                else:
                    next_game(m, w)
        self.assertEqual(m.get_count(), 4)  # add assertion here


if __name__ == '__main__':
    unittest.main()
