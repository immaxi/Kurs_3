from abc import ABC, abstractmethod

class Figure(ABC):
    """ Абстрактный класс 'Геометрическая фигура' """

    @abstractmethod

    def square(self):
        """ Содержит виртуальный метод для вычисления площади фигуры """

        pass
