
from lab_python_oop.Rectangle import Rectangle

class Square(Rectangle):
    """Класс 'Квадрат' наследуется от класса 'Прямоугольник'"""

    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls):
        return cls.FIGURE_TYPE

    def __init__(self, color, side):
        self.side = side
        super().__init__(color, side, side)

    def __repr__(self):
        return f"{Square.get_figure_type()} {self.fc.colorproperty} цвета со стороной {self.side} площадью {self.square()}"