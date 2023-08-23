class Point:
    "Класс для представления координат точек на плоскастиd"
    color = 'red'
    circle = 2


a = Point()
a.x = 1
a.y = 2

b = Point()
b.x = 10
b.y = 20

print(a.__dict__)
print(b.__dict__)

print(Point.__doc__) # Получаем док класс (описание)
