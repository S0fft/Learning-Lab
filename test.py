class Point:
    color = 'red'
    circle = 2

    def set_cords(self, x, y):
        self.x = x
        self.y = y

        print(f"Вызов метода set_cords для {self}")

    def get_cords(self):
        return f"OBJ: {self} - {(self.x, self.y)}"


# Point.set_cords() # Не сработает, пока есть параметр self

pt = Point()

pt2 = Point()
print(pt.__dict__)

pt.set_cords(1, 2)
print(pt.__dict__)

pt2.set_cords(10, 20)
print(pt2.__dict__)

print(pt.get_cords())
print(pt2.get_cords())

f = getattr(pt, 'get_cords')  # Сохранение метода get_cords экземпляра pt в переменной, c возможным подальшем вызовом
print(f())
