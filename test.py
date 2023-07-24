class ParentClass:
    def some_method(self):
        print("Вызван метод родительского класса")

class ChildClass(ParentClass):
    def some_method(self):
        super().some_method()  # Вызываем метод родительского класса
        print("Вызван метод дочернего класса")

child = ChildClass()
child.some_method()
