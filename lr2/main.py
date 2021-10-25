from lab_python_oop.Rectangle import Rectangle
from lab_python_oop.Square import Square
from lab_python_oop.Circle import Circle

def main():
    r = Rectangle("синего", 5, 5)
    s = Square("зеленого", 5)
    c = Circle("красного", 5)
    print(r)
    print(s)
    print(c)
    input("Нажмите Enter для продолжения")

if __name__ == "__main__":
    main()
