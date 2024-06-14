import csv  # Работа с csv файлами
import json  # Работа с JSON форматом
import math  # Работа с матемтическми выражениями
import random  # Работа с псевдо-рандомными значениями
import re  # Регулярные выражения
import secrets  # Работа с полностью рандомными значениями
import smtplib  # Работа с отправкой сообщений по СМПТ
import sqlite3  # Работа с SQL-lite и DB-browoser
import string  # Работа с различными символами (строки, цифры)
import sys  # Работа с аргументами программы
import time  # Работа с временностью выполнения кода
import webbrowser  # Работа с веб-браузером
from array import array  # Работа с типизированными массивами
from datetime import date, datetime, time, timedelta  # Работа с датой и временем
from email.message import EmailMessage  # Работа с отправкой сообщений по СМПТ
from functools import wraps
from os import path  # Функциональный подход работы с файлами
from pathlib import Path  # ООП подходит работы с файлами
from string import Template  # Работа с отправкой сообщений по СМПТ


# ------- СОЗДАНИЯ СЛОВАРЯ ИЗ СПИСКОВ С ПОМОЩЬЮ ZIP:
def my_fn(one, two):
    return dict(zip(one, two))


my_fn(one=["first", "second"], two=[1, 2])  # {'first': 1, 'second': 2}
my_fn(["first", "second"], [1, 2])  # {'first': 1, 'second': 2}


# ------- СОЗДАНИЯ СЛОВАРЯ ИЗ АРГУМЕНТОВ С КЛЮЧИВЫМИ СЛОВАМИ И ** ПАРАМЕТРА:
def first_my_fn(**keys):
    keys["year"] = 2024
    return keys


# first_my_fn(mark="Honda", price=10000)  # {'mark': 'Honda', 'price': 10000, 'year': 2024}

# ------- ОБЬЕДИЕНИЕ СЛОВАРЕЙ С ПОМОЩЬЮ ** И МЕТОДА:
button = {
    "width": 200,
    "text": "Buy",
    "color": "green",
}

red_button = {
    **button,  # Значение color останится "red", если указать ниже 27 строки - значение прещапишется на "green"
    "color": "red",
}

# print(button)  # {'width': 200, 'text': 'Buy', 'color': 'green'}
# print(red_button)  # {'width': 200, 'text': 'Buy', 'color': 'red'}

button_info = {
    "text": "Buy",
    "color": "black",
    "width": 0,
    "height": 0,
}

button_style = {
    "color": "yellow",
    "width": 200,
    "height": 300,
}

result_button = {  # Распаковка двух словарей в один
    **button_info,
    **button_style
}
# ИЛИ
result_button = button_info | button_style  # Вывод: значения второго, т.к значения первого перезаписываются

# print(result_button)  # {'text': 'Buy', 'color': 'yellow', 'width': 200, 'height': 300}

first_dict = {
    "key_one": 1,
    "key_two": 2,
}

second_dict = {
    "key_one": 3,
    "key_two": 4,
}

third_dict = {
    "key_one": 5,
    "key_two": 6,
}

new_dict = {
    **first_dict,
    ** second_dict,
    ** third_dict,  # Значения послденего презаписываю все остальные ({'key_one': 5, 'key_two': 6})
}
# ИЛИ
new_dict = first_dict | second_dict | third_dict

# print(new_dict)  # {'key_one': 5, 'key_two': 6}


#  ------- ИНСТРУКЦИЯ DEL:
my_list = [1, 2]

del my_list[0]  # del это инструкция - удаляет ПО ИНДЕКСУ
# ИЛИ
my_list.__delitem__(0)

# print(my_list) []


#  ------- СТРОКИ И FSTRINGS:
my_name = "yevhen"
my_hobby = "running"
time = 8

result_simple_string = my_name + " " + "likes" + " " + my_hobby + " " + "at" + " " + str(time) + " " + "clock"
# ИЛИ
result_f_strng = f"{my_name} likes {my_hobby} at {time} o'clock!"

# print(result_f_strng.capitalize()) # Yevhen likes running at 8 o'clock!
# print(result_simple_string) # yevhen likes running at 8 clock


# ------- LAMDA ФУНКЦИЯ:
def mult(a, b):
    return a * b


# ИЛИ
lambda a, b: a * b  # Ключивое слово - парметры - тело функции


def greeting(greet):
    return lambda name: f"{greet}, {name}!"


mroning_greeting = greeting("Good Morning")  # Вызываем функцию greeting, сохроняем результат в пременную
# print(mroning_greeting)
# print(mroning_greeting("Yevhen"))  # Вызываем переменную "результат", в результате вызывается лямбда функция,
# которой нужно ввести аргумент name. Это называется замыкание.

evening_greeting = greeting("Good Evenig")
evening_greeting("Yevhen")


#  ------- ОБРАБОТКА ОШИБОК
try:
    # Выполнение кода
    pass
except TypeError:  # Обработка ошибки TypeError
    # Выполняется в случае ошибки в блоке try
    pass

try:
    print("10" / 0)
except ZeroDivisionError as e:  # Если эта ошибка - выводится тело первого except
    # print(type(e))
    # print(e)
    pass
except TypeError as e:  # Если эта ошибка - выводится тело второго except
    # print(type(e))
    # print(e)
    pass
else:  # Выполняется если ошибок не возникло
    # print("There was no error")
    pass
finally:  # Выполняется в любом случае
    # print("Finish")
    pass

# print("Continue")

# Если ошибка предварительнно не известна:
try:
    # print(10 / 0)
    pass
except Exception as e:
    # print(isinstance(e, ZeroDivisionError))
    # print(e)
    pass
# ИЛИ
try:
    # print(10 / 0)
    pass
except:
    # print("Some error")
    pass


# Генерация ошибок (чтобы в будущем отлавить ее)
def divide_nums(a, b):
    if b == 0:
        raise ValueError("Second argument can't be 0!")  # Генерация ошибки (генерация ошибки чтобы отлавить ее по типу)
    return a / b


# print(divide_nums(10, 0))
try:
    divide_nums(10, 0)
except ZeroDivisionError as e:  # Ошибка уже сформированна, поэтому блок не сработает
    # print(e)
    pass
except ValueError as e:  # Отлавливание снегерированной ошибки
    # print(e, "WOW")
    pass


my_dict = {
    "image_title": "my_car",
    "image_id": 232,
    "image_likes": 10000,
}


# Обработка ошибки
def image_info(dict):
    if "image_title" and "image_id" in dict:
        return f"Image {dict['image_title']} has id {dict['image_id']}"
    else:
        raise TypeError("Dict dosen't have these itemes")


try:
    # print(image_info(my_dict))
    pass
except TypeError as e:
    # print(e)
    pass
del my_dict["image_id"]

try:
    # print(image_info(my_dict))
    pass
except TypeError as e:
    # print(e)
    pass


#  ------- РАСПАКОВКА СПИСКОВ И КОРТЕЖЕЙ В ПЕРЕМЕННЫЕ
my_list_new = [1, 2, 3]

first, second, third = my_list_new
# print(first)
# print(second)
# print(third)
# ИЛИ
first, *second_list = my_list_new  # Разбиение первого элемента отдельно, остальные в новый список
# print(first)
# print(second_list)


#  ------- РАСПАКОВКА СЛОВАРЕЙ С ПОМОЩЬЮ ФУНКЦИИ И **
user_profile = {
    "name": "Yevhen",
    "comments_qty": 23,
    "id": 232,
}


def user_info(name, comments_qty=0, id=0):
    if not comments_qty:  # Если переменная НЕ равна True - выводится тело условного оператора.
        return f"{name} has no comments"

    return f"{name} has {comments_qty} comments"


# name, comments_qty = user_profile # Распаковка КЛЮЧЕЙ словаря
# print(name) # name
# print(user_info(**user_profile))  # Распаковка словаря (2 параметра - 2 ключа)
# print(user_info(user_profile["name"], user_profile["comments_qty"]))  # Распаковка по позиционным значениям
# print(user_info(comments_qty=user_profile["comments_qty"], name=user_profile["name"]))  # Распковка по ключивым
# значениям


# ------- РАСПАКОВКА СПИСКОВ С ПОМОЩЬЮ ФУНКЦИИ И *
user_data = ["Yevhen", 23]


def second_user_info(name, commnets_qty=0):
    if not commnets_qty:
        return f"{name} has no comments"

    return f"{name} has {commnets_qty} comments"


my_name, my_comments_qty = user_data
# print(my_name)

# print(second_user_info(*user_data))
# print(second_user_info(user_data[0], user_data[1]))
# print(second_user_info(name=user_data[0], commnets_qty=user_data[1]))

list_dicts = [
    {"first": "one", "second": "two"},
    {"id": 111, "likes": 2443},
    {"bread": 10, "milk": 20}
]

first_d, second_d, third_d = list_dicts
# print(first_d)


def my_fun(first, second):  # Параметры должны сооствсовать именем и количестовм ключей в словаре
    return f"{first} and {second}"


# print(my_fun(**first_d))
# print(my_fun(first=second_d["id"], second=second_d["likes"]))
# print(my_fun(second_d["id"], second_d["likes"]))
# print(my_fun(first=third_d["bread"], second=third_d["milk"]))
# print(my_fun(**third_d))


# ------- УСЛОВНЫЕ ИНСТРУКЦИИ IF
person_info = {
    "age": 20,
    "name": "Yevhen"
}


if not person_info.get("name"):  # Результат выражения с оператором not и ложным опернадом - всегда True
    print("No name")
else:
    # print(person_info["name"])
    pass

my_number = 21.5
if type(my_number) is int:
    print(my_number, "is integer")
else:
    # print(my_number, "is not an integer")
    pass

my_phone = {
    "price": 200,
    # "brand": "HTC"
}

if my_phone.get("brand"):
    print("Phone's brand is", my_phone["brand"])
else:
    # print("There is no phone brand")
    pass


def nums_info(a, b):  # Читабильный вариант функции с IF
    if (type(a) is not int) or (type(b) is not int):
        return "Один из аргументов не целое число!"

    if a >= b:
        return f"{a} больше либо равно {b}"

    return f"{a} меньше {b}"


# print(nums_info(True, 10))
# print(nums_info(10, 2))
# print(nums_info(4, 15))


def nums_info_new(a, b):
    if (type(a) is not int) or (type(b) is not int):
        info = "Один из аргументов не целое число!"
    elif a >= b:
        info = f"{a} больше либо равно {b}"
    else:
        info = f"{a} меньше {b}"
    return info


# print(nums_info_new(True, 10))
# print(nums_info_new(10, 2))
# print(nums_info_new(4, 15))


def route_info(dict):
    if type(dict.get("distance")) is int:
        return f"Distance to your destination {dict['distance']}"
    elif type(dict.get("speed")) is int and type(dict.get("time")) is int:
        return f"Distance to your destination is {dict['speed'] * dict['time']}"
    else:
        return "No distace info is available"


# print(route_info({"distance": 100}))
# print(route_info({"speed": 2, "time": 2}))
# print(route_info({"brand": "Honda"}))


# ------- ТЕРНАРНЫЙ ОПЕРАТОР
my_number = 21.5

# print("is int") if type(my_number) is int else print("is not int")  # "Пиши если "is int" тип переменной инт
# иначе пиши "is not int"

# send_img(img) if img.get("is processed") else process_and_send_img(img)

product_qty = 10

# print("in stock" if product_qty > 0 else "out of stock")

temp = +24
weather = "hot" if temp > 18 else "cold"

my_img = ("1920", "1080")

# print(my_img[0], "x", my_img[1]) if len(my_img) == 2 and type(my_img[0]) is str and type(my_img[1]) is str else
# print("Not correct")
# Печатай первый x второй индекс если длинна списка = 2 и тип первого и второго элемента строки иначе печайт "Not"

info = f"{my_img[0]} x {my_img[1]}" if len(my_img) == 2 and type(my_img[0]) is str and type(my_img[1]) is str else "Not"
# print(info)


if len(my_img) == 2 and type(my_img[0]) is str and type(my_img[1]) is str:
    # print(f"{my_img[0]} x {my_img[1]}")
    pass
else:
    # print("Not correct")
    pass

my_new_string = "wdwdwdwdwwwwdwdwdwssdddddddddddddddddddddddddddddddddddddddddddddddddddddddddwdw"
# print("sring is long") if len(my_new_string) > 79 else print("string is short")


# ------- ЦИКЛЫ
my_new_dict = {
    "x": 10,
    "y": True,
    "z": "abc",
}

for key in my_new_dict:
    # print(key, ":", my_new_dict[key])  # Вывод ключа а полсе значения словаря
    pass

for item in my_new_dict.items():
    key, value = item
    # print(key, value)
# ИЛИ
for key, value in my_new_dict.items():
    # print(key, value)
    pass


def dict_to_list(dict):
    result = []
    for k, v in dict.items():
        if type(v) is int:
            v * 2
            result.append((k, v))
        else:
            result.append((k, v))
    return result


# print(dict_to_list(my_new_dict))


def filter_list(list_to_filter, type_of_data):
    for t in range(len(list_to_filter)):
        for i in list_to_filter:
            if type(i) is not type_of_data:
                list_to_filter.remove(i)

    return list_to_filter


# print(filter_list([35, True, "abc", 10], int))


def filter_new_list(list_to_filter, value_type):
    def check_element_type(elem):
        return isinstance(elem, value_type)  # Вернуть элементы, которые соответствуют value_type

    # Пробегаемся функцией по списку и возращаем значения которые соотвествуют value_type
    # return list(filter(check_element_type, list_to_filter))
    # ИЛИ              Получаем элементы с нужным классом
    return list(filter(lambda elem: type(elem) is value_type, list_to_filter))
    return list(filter(check_element_type, value_type))
    # Запечатываем с ловарь - вызываем функци filter -
    # создаем lmbda функцию которая будет возращать соответствующие элементы из list_to_filter


# print(filter_new_list([1, 10, "abc", True, 5.5], int))


# ------- ЦИКЛ WHILE:
# while True:
#     answer = input("Enter yes or no: ")
#     if answer == "no":
#         break

# random_num = random.randint(1, 5)

# while True:
#     num = int(input("Enter your number: "))
#     if num != random_num:
#         print("Try again!")
#         continue
#     else:
#         print("Yes!")
#         break

# while True:
#     num_frist = int(input("Please, enter first number: "))
#     num_second = int(input("Please, enter second number: "))
#     if num_frist == 0 or num_second == 0:
#         print("Condition zero!")
#         continue
#     print(num_frist / num_second)
#     answer = input("Do you want to contuniue? (yes/no): ")
#     if answer == "no":
#         break
#     else:
#         continue


# ------- Сокращенный цикл for in (Comprehension):
all_nums = [-3, 1, 0, 1, -20, 5]
absolute_nums = []

for num in all_nums:
    # absolute_nums.append(abs(num))
    pass

# ИЛИ

absolute_nums = [abs(num) for num in all_nums]  # Форумируем список, пропуская все эелементы через abs()
# print(absolute_nums)


all_nums = [-3, 1, 0, 1, -20, 5]
positive_nums = []

for num in all_nums:
    if num > 0:
        positive_nums.append(num)

# ИЛИ

positive_nums = [num for num in all_nums if num > 0]
# print(positive_nums)


my_set = {1, 10, 15}
new_set = set()

for val in my_set:
    # new_set.add(val * val)
    pass

# ИЛИ

my_set = {val * val for val in my_set}
# print(my_set)

my_scores = {
    "a": 10,
    "b": 7,
    "m": 14,
}

scores = {}

for k, v in my_scores.items():
    # scores[k] = v * 10
    pass

# ИЛИ

scores = {k: v * 10 for k, v in my_scores.items()}


my_new_list = [10, 7, 14]

result = {k: v * 2 for k, v in enumerate(my_new_list) if v > 7}

# print(result)


new_my_dict = {
    "one": "first",
    "two": "second",
}

new = {k: v.upper() for k, v in new_my_dict.items()}
# print(new)


new_new = {}

for k, v in new_my_dict.items():
    new_new[k] = v.upper()

# print(new_new)


task_one_list = ["ogo", "aga", "ugu", "hello", "hi"]

list_str = [elem for elem in task_one_list if len(elem) > 3]
# print(list_str)


# squares_gen = (num * num for num in range(100_000_000))  # Маленький размер в памяти, не смотря на обьем данных.

# print(getsizeof(squares_gen))  # 104 size


# squares_list = [num * num for num in range(100_000_000)]

# print(getsizeof(squares_list))  # 835128600 size


# ------- ФИБОНАЧИ:
n = 10

x1 = 1
x2 = 1

for i in range(n):
    # print(x1, end=" ")
    x1 = x2
    x2 = x1 + x2

# ТРИБОНАЧИ

x1 = 1
x2 = 1
x3 = 1

for i in range(n):
    # print(x1, end=" ")
    x1, x2, x3 = x2, x3, x1 + x2 + x3


# ---------------------------------ООП

class Car:
    def move(self):
        print("Car is moving")

    def stop(self):
        print("Car is stopped")


my_car = Car()
my_second_car = Car()

# print(type(my_car))
# print(isinstance(my_car, Car))

# my_car.move()
# my_car.stop()

# print(my_car.__dict__)

# print(my_car == my_second_car)
# print(id(my_car), id(my_second_car))

# Car.move(my_car)


class Comment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self, qty):
        self.votes_qty += qty

    def reset_votes_qty(self):
        self.votes_qty = 0


my_comment = Comment("My_comment")
# # print(my_comment)
# print(type(my_comment))
# print(my_comment.__dict__)
# print(dir(my_comment))

# print(my_comment.text)
# print(my_comment.votes_qty)

# my_comment.upvote(2)
# print(my_comment.votes_qty)

# my_comment.upvote(10)
# print(my_comment.votes_qty)

my_comment.upvote(10)
# print(my_comment.__dict__)

my_comment.upvote(20)
# print(my_comment.__dict__)

my_comment.reset_votes_qty()
# print(my_comment.__dict__)


class Image:
    def __init__(self, resolution, title, extension):
        self.resolution = resolution
        self.title = title
        self.extension = extension

    def resize(self, new_res):
        self.resolution = new_res

    def retitle(self, new_title):
        self.title = new_title


my_image = Image("1980 x 1020", "LG", "24")
# print(my_image.__dict__)

my_image.resize("2400 x 1200")
# print(my_image.__dict__)

my_new_image = Image("480 x 240", "AOC", "21")
# print(my_new_image.__dict__)

my_new_image.resize("1360 x 768")
# print(my_new_image.__dict__)

# print(my_image.__dict__)

my_image.retitle("Samsung")
# print(my_image.__dict__)

my_new_image.retitle("Benq")
# print(my_new_image.__dict__)


class NewComment:
    total_comments = 0

    def __init__(self, text):
        self.text = text
        NewComment.total_comments += 1

    @staticmethod
    def merge_comments(first, second):
        return f"{first} {second}"


my_new_comment = NewComment("My comment")
my_new_comment_second = NewComment("My new comment")

m_1 = my_new_comment.merge_comments("Thanks!", "excelent")
# print(m_1)

m_2 = my_new_comment.merge_comments("Great", "Ok")
# print(m_2)

my_new_comment.total_comments = 10
NewComment.total_comments = 22

# print(NewComment.total_comments)
# print(my_new_comment.total_comments)


# ------------------МАГИЧЕСКИЕ МЕТОДЫ

class LastComment:
    def __init__(self, text):
        self.text = text
        self.votes_qty = 0

    def upvote(self):
        self.votes_qty += 1

    def __add__(self, other):
        return (f"{self.text} {other.text}", self.votes_qty + other.votes_qty)


first_comment = LastComment("Hello")
second_comment = LastComment("Bye")

first_comment.upvote()
second_comment.upvote()

# print(first_comment + second_comment)


class ExtendedList(list):
    def print_list_info(self):
        pass
        # print(f"list has {len(self)} elements")


custom_list = ExtendedList([3, 5, 2])
custom_list.print_list_info()

custom_list.append(3)
custom_list.print_list_info()


class Soda():
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None

    def show_my_drink(self):
        if self.ingredient:
            # print(f"Cola and {self.ingredient}")
            pass
        else:
            # print("Simple Cola")
            pass


# drink1 = Soda()
# drink2 = Soda('lime')
# drink3 = Soda(5)
# drink1.show_my_drink()
# drink2.show_my_drink()
# drink3.show_my_drink()


class TriangleChecker():
    def __init__(self, first_side, second_side, third_side):
        self.first_side = first_side
        self.second_side = second_side
        self.thrid_side = third_side

    def is_triangle(self):
        if type(self.first_side) is not int or type(self.second_side) is not int or type(self.thrid_side) is not int:
            return "Use only numbers!"

        if self.first_side < 0 or self.second_side < 0 or self.thrid_side < 0:
            return "It won't work with negative numbers."

        if self.first_side + self.second_side <= self.thrid_side:
            return "We don't can build the triangle with this sides!"
        elif self.thrid_side + self.second_side <= self.first_side:
            return "We don't can build the triangle with this sides!"
        elif self.first_side + self.thrid_side <= self.second_side:
            return "We don't can build the triangle with this sides!"
        else:
            return "Yes! We can build the triangle!"


# triangle1 = TriangleChecker(2, 3, 4)
# print(triangle1.is_triangle())
# triangle2 = TriangleChecker(77, 3, 4)
# print(triangle2.is_triangle())
# triangle3 = TriangleChecker(77, 3, 'Side3')
# print(triangle3.is_triangle())
# triangle4 = TriangleChecker(77, -3, 4)
# print(triangle4.is_triangle())

class Vehicle():
    def __init__(self, name,  max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage


model_x = Vehicle("Skoda", 240, 17)


class Transport():
    pass


class Bus(Vehicle):
    pass


school_bus = Bus("Volvo", 180, 12)
# print(f"Name: {school_bus.name}, Max-Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")


class Point:
    # Атрибуты класса/свойства класса
    color = "red"
    circle = 2

    def set_cords(self, x, y):
        self.x = x
        self.y = y

    def get_cords(self):
        return (self.x, self.y)


Point.color = "black"

a = Point()
b = Point()

a.color = "green"
Point.type_pt = "disk"
setattr(Point, "prop", 1)

setattr(Point, "type_pt", "square")

del Point.prop

getattr(Point, "prop", False)

pt = Point()
pt.set_cords(1, 2)

pt2 = Point()
pt2.set_cords(10, 20)

cords1 = getattr(pt, "get_cords")
# print(pt2.__dict__)

# ---------------------SINGLETON
class DataBase:
    __instance = None  # Ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f"соединение c БД: {self.user}, {self.psw}, {self.port}")

    def colse(self):
        print("Закрытие cоединения с БД")

    def read(self):
        return "данные из БД"

    def write(self, data):
        print(f"запись в БД  {data}")


db = DataBase("root", 1234, 80)
db2 = DataBase("root2", 5678, 40)
# print(id(db), id(db2))


# -------------------ДЕКОРАТОРЫ @classmethod и @staticmethod

class Vector:
    MIN_CORD = 0
    MAX_CORD = 100

    @classmethod  # Метод только для класса
    def validate(cls, arg):
        return cls.MIN_CORD <= arg <= cls.MAX_CORD  # Попадает ли arg в диапазон

    def __init__(self, x, y):
        self.x = 0
        self.y = 0
        if self.validate(x) and self.validate(y):
            self.x = x
            self.y = y

        # print(self.norm2(self.x, self.y))

    def get_cord(self):
        return self.x, self.y

    @staticmethod  # Используется БЕЗ ссылок на класс и экземпляр
    def norm2(x, y):
        return x*x + y*y


v = Vector(10, 20)
# print(Vector.norm2(5, 6))


# -------------ИНКАПСУЛЯЦИЯ

class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    @classmethod
    def __check_value(cls, x):
        return type(x) in (int, float)

    def set_coord(self, x, y):
        if self.__check_value(x) and self.__check_value(y):
            self.__x = x
            self.__y = y
        else:
            raise ValueError("Кординаты должны быть числами!")

    def get_cord(self):
        return self.__x, self.__y


pt = Point()
pt.set_coord(10, 20)
# print(pt.get_cord())
# pt.__check_value(5)


# --------------------ООП ПРАКТИКА

class Vehicle:
    def __init__(self, name, max_speed, milage):
        self.color = "white"
        self.name = name
        self.max_speed = max_speed
        self.milage = milage

    def seating_capacity(self, capacity):
        return f"Вместимость {self.name} - {capacity}"

    def fare(self):
        return self.capacity * 100


car_model = Vehicle("Skoda", 299, 100)
# print(car_model.name, car_model.max_speed, car_model.milage)
# print(car_model.__dict__)


class Bus(Vehicle):
    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity)

    def fare(self):
        return super().capacity * 100


bus_model = Bus("Volvo", 130, 70)
# print(bus_model.seating_capacity(70))
# print(bus_model.__dict__)
# print("Total Bus fare is:", bus_model.fare())

# ----------------------------------------RE

s = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"
d = "AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC"

res = re.match("AC", s)  # Ищет заданный шаблон в начане строки
res1 = re.search("DC", s)  # Ищет заданный шаблон по всей строке, возращает первый найденный
res2 = re.findall("DC", s)  # Ищет заданный шаблон и формирует список с заданным шабоном
res3 = re.split("/", s, maxsplit=3)  # Разбивает строку по заданному символу 3 раза
res4 = re.sub("A", "D", s)  # Заменяет указанный символ на второй аргумент (A на D)
res5 = re.fullmatch(s, d)  # Сравнивает строки на полное соответствие


# print(res)  # <re.Match object; span=(0, 2), match='AC'>
# print(res1)  # <re.Match object; span=(3, 5), match='DC'>
# print(res1[0])  # DC
# print(res2)  # ['DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'DC', 'DC']
# print(res3)  # ['AC', 'DCAC', 'DCAC', 'DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC']
# print(res4)  # DC/DCDC/DCDC/DCDC/DCDC/DCDC/DCDC/DCDC/DCDC/DC
# print(res5)  # <re.Match object; span=(0, 45), match='AC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DCAC/DC'>

new_s = "87+8845 abcd    ---- kjgfj373^JEFHEJFJqqqq"

res01 = re.search(r"a..d", new_s)  # Находит последовательность от а до d, между которыми два символа
res02 = re.search(r"\d\d\d", new_s)  # Выводит первую попавшиюся цифру в строке (если один \d) / 3 цифры подряд
res03 = re.search(r"\s", new_s)  # Выводит первый попавшися пробел (или несколько пробелов пордряд если \s\s)
# Выводит первый попавшися НЕ пробелильный символ (или несколько символов пордряд если \S\S)
res04 = re.search(r"\S", new_s)
# Выводит первую попашиюся цифру/буквы либо _ (или несколько символов пордряд если \w\w\w)
res05 = re.search(r"\w", new_s)
# Выводит первую попашиюся НЕ цифру/НЕ букву  (или несколько символов пордряд если \W\W\W)
res06 = re.search(r"\W", new_s)
res07 = re.search(r"\bkjgf", new_s)  # Выводит начало слова по символьно (с какого индекса начинается слово)
res08 = re.search(r"\B kjgf", new_s)  # Выводит заданаю подстроку от буквы до буквы в строке (в середине)
res09 = re.search(r"\d* ", s)

# print(res01[0])  # abcd
# print(res02[0])  # 884
# print(res03[0])  # " "
# print(res04[0])  # 8
# print(res05[0])  # 8
# print(res06[0])  # +
# print(res07[0])  # kjgf
# print(res08[0])  # " "kjgf


# ---------------------JSON

json_str = '{"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": "true"}}'
# print(type(json_str), json_str)  # <class 'str'> {"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": "true"}}

json_to_dict = json.loads(json_str)
# print(type(json_to_dict), json_to_dict)
# <class 'dict'> {'id': 235, 'brand': 'Nike', 'qty': 84, 'status': {'isForSale': 'true'}}

new_json = json.dumps(json_to_dict)
# print(type(new_json), new_json)  # <class 'str'> {"id": 235, "brand": "Nike", "qty": 84, "status": {"isForSale": "true"}}
# (С отступами)

dict_j = {
    "first": "one",
    "second": 2,
    "third": True,
    "d": {
        "lst": (1, 2, 3, 4)
    }
}


dict_j_to_json = json.dumps(dict_j)  # , indent=1)
# print(type(dict_j_to_json), dict_j_to_json)  # <class 'str'> {"first": "one", "second": 2, "third": true}

to_dict = json.loads(dict_j_to_json)
# print(type(to_dict), to_dict)  # <class 'dict'> {'first': 'one', 'second': 2, 'third': True}

# --------------РАБОТА С ФАЙЛАМИ

# from os import path  # Функциональный подход работы с файлами
# from pathlib import Path  # ООП подходит работы с файлами

# - Функциональный подход
# print(path.abspath("."))  # Вывод текущей дириктории
# print(type(path))

# - ООП подход
# print(Path(".").absolute())  # Вывод текущей дириктории
# print(type(Path))

# file_path = Path("test.txt")  # Создание и название файла (относительный путь к файлу)

# print([m for m in dir(file_path) if not m.startswith("_")])  # Вывод всех атрибутов экземпляра, имя которых не начинается на _

# print(Path.cwd())  # Вывод текущей дириктории методом класса (cwd - Curent Working Directory)

# # - Формирование путей на MAC и UNX
# print(Path("usr").joinpath("local").joinpath("bin"))  # usr\local\bin
# # ИЛИ
# print(Path("usr") / "local" / "bin")  # usr\local\bin

# # - Формирование путей на Windows
# print(Path("C:/").joinpath("Users").joinpath("yevhen"))  # C:\Users\yevhen
# # ИЛИ
# print(Path("C:/") / "Users" / "yevhen")  # C:\Users\yevhen

# # - Проверка на сущестования дириктории/файла
# print(Path("test.py").exists())  # False

# print(Path("Desktop").exists())  # False

# # - Проверка на "является ли файлом"
# print(Path("main.py").is_file())  # True
# # (Нужно указывать абсолютный путь)

# print(Path("../PYTHON").is_file())  # Выход на один уровень выше (..) и проверка папки

# print(Path("../PYTHON").is_dir())  # Выход на один уровень выше (..) и поиск ДИРИКТОРИИ

# for f in Path(".").iterdir():
#     print(f)  # Вывод всех папок/файлов в текущей (".") дириктории

cwd = Path(".") / "gg"

if not cwd.exists():
    # cwd.mkdir()  # Если файл не существут - создаем
    pass

if cwd.exists():
    # cwd.rmdir()  # Если файл существует - удаляем
    pass

# print(Path(".").cwd())  # Вывод текущей дириктории

# with open("test.txt") as test_file:
#     # print(test_file.read())  # Чтение данных из файлов
#     pass

# with open("test.txt", "a") as test_file:
#     # test_file.write("allo\n")  # Добавление данных в файл
#     pass


# with open("new.txt", "w") as new_file:
#     # new_file.write("New STR")  # Перезапись данных в файле
#     pass

# - Альтернативный вариант
# test_file = open("test.txt", "w")

# test_file.write("First string\n")
# test_file.write("Second string\n")

# test_file.close()

# test_file = open("test.txt")

# print(test_file.read())

# ------------ ПРАКТИКА РАБОТЫ С ФАЙЛАМИ


# files_dir = Path("files")
# files_dir.mkdir(exist_ok=True)

# first_file = files_dir / "first.txt"
# second_file = files_dir / "second.txt"

# with open(first_file, "w") as f:
#     f.write("First_String \n")
#     f.write("Second_String \n")

# with open(second_file, "w") as f:
#     lines = [
#         "one",
#         "two",
#         "three"
#     ]
#     for line in lines:
#         f.write(line + "\n")


# with open(files_dir / "first.txt") as f:
#     print(f.read())

# with open(files_dir / "second.txt") as f:
#     for line in f:
#         print(line.strip())
#     # - ИЛИ
#     # while True:
#     #     line = f.readline()
#     #     if not line:
#     #         break
#     #     print(line.strip())

# first_file.unlink()
# second_file.unlink()

# files_dir.rmdir()

# ------ZIP файлы

# if not Path("my_files").exists():
#     Path("my_files").mkdir()

#     with open("my_files/first.txt", "w") as my_file:
#         my_file.write("This is first file")

#     with open("my_files/second.txt", "w") as my_file:
#         my_file.write("This is second file")


# with ZipFile("my_files.zip", mode="w") as my_zip_file:
#     for file in Path("my_files").iterdir(): # Запись файлов в архив
#         my_zip_file.write(file)

# with ZipFile("my_files.zip") as my_zip_file:
# my_zip_file.extractall("my_files-unzipped")  # Распаковка архива в папку my_files-unzipped
# print(my_zip_file.infolist())
# print(my_zip_file.filename)


# ------------CSV

# if not Path("test.csv").exists():
#     with open("test.csv", "w") as csv_file:
#         writer = csv.writer(csv_file, delimiter=";")
#         writer.writerow(["user_id", "user_name", "commands_qty"])
#         writer.writerow([5235, "yevhen", 123])
#         writer.writerow([453, "mike", 423])
#         writer.writerow([1357, "alice", 245])

# with open("test.csv") as csv_file:
#     reader = csv.reader(csv_file, delimiter=";")
#     csv_list = list(reader)
#     print(csv_list)


# ------------ДАТА

# my_date = date(2110, 4, 15)
# print(my_date)  # 2110-04-15

# print(my_date.day)  # 15
# print(my_date.month)  # 4
# print(my_date.year)  # 2110
# print(my_date.isocalendar())  # datetime.IsoCalendarDate(year=2110, week=16, weekday=2)

# my_time = time(18, 10, 45)
# print(my_time)

# print(my_time.hour)  # 18
# print(my_time.minute)  # 10
# print(my_time.second)  # 45

# my_datetime = datetime(2222, 12, 10, 18, 10, 45)
# print(my_datetime)  # 2222-12-10 18:10:45

# print(my_datetime.year)  # 2222
# print(my_datetime.hour)  # 18
# print(my_datetime.second)  # 45
# print(my_datetime.microsecond)  # 0

# print(my_datetime.now())  # 2023-02-25 10:54:19.037999

# -----Форматирование даты

new_data = datetime(2222, 12, 10, 18, 10, 45)

# print(new_data.strftime("%d-%m-%Y"))
# print(new_data.strftime("%d-%b-%Y %H:%M:%S"))  # День, месяц, год, час, минуты, секунды

date_str = "10/12/2222"

converted_date = datetime.strptime(date_str, "%d/%m/%Y")

# print(converted_date)

# print(new_data + timedelta(days=100, hours=2, minutes=120))  # Добавление к дате 100 дней, 120 минут

# ------ TIME

# start_time = time.time()
# print(time.time())  # Текушие время в секунднах с начала юникс эпохи (1 января, 1970) года
# print(time.ctime(23445465724))  # Добавление секунд к текущем юникс-времени

# time.sleep(2.5)  # остановка времени на 2.5 секунды

# end_time = time.time()
# print("Total time: ", end_time - start_time)  # Время выполнения кода


# --------МОДУЛЬ RANDOM

# print(random.random())  # Генерация числа до 1

# print(random.randint(1, 10))  # Генерация чис от 1 до 10 включительно

# print(random.choice("abcd"))  # Выбор одного случайного элемента в последовательности

# print(random.choices(["a", "b", "c", "d"], k=2))  # Выбор нескольких (2) случайных элементов в последовательности

new_lst = [1, 2, 3, 4, 5]
random.shuffle(new_lst)  # Перемешивает элементы внутри списка
# print(new_lst)

# print(random.choices("0123456789", k=8))  # Соеденяет в строку последовательности и перемешивает 8 элементов, создавая список
# print("".join(random.choices("0123456789", k=8)))  # Соеденяем все в строку
# Random генерирует псевдо-случаенные значения


# ----------- SECRTETS И STRING

# print(string.ascii_letters)  # Вывод всех букв в двух регистрах
# print(string.digits)  # Вывод всех цифр
# print(string.punctuation)  # Вывод всех спец. символов

# print(string.ascii_lowercase)  # Вывод букв в нижнем регистре
# print(string.ascii_uppercase)  # Вывод букв в верхнем регистре

all_chars = string.ascii_letters + string.digits + string.punctuation
# print(all_chars)  # Вывод абсолютно всех символов

# print("".join(secrets.choice(all_chars) for i in range(8)))  # Фомирования пароля с 8 символами


# ---------- MATH
# print(math.pi)  # Вывод PI
# print(math.e)  # Вывод E

# print(math.sqrt(25))  # Вывод корня из 25 в флот (5)
# print(math.log(100))  # Вывод логорифма из 100

# print(math.factorial(10))  # Уможение каждого последушего элемента (10 * 9, 10 * 8..)

# print(dir(math))  # Вывод всех атрибутов в модуле math


# ------------- ФАКТОРИАЛ - РЕКУРСИЯ
def calc_factorial(num):
    if type(num) is not int:
        raise TypeError("Number must be integer")

    if num <= 0:
        raise ValueError("Number must be positive")

    if num == 1:
        return 1

    return calc_factorial(num-1) * num


calc_factorial(10)


# ----------------------re

my_string_name = "My name is Yevhen."

res26 = re.search(r"Yevhen", my_string_name)  # Поиск строки Yevhen в строке
res27 = re.search(r"Y....n$", my_string_name)  # Точка - пропущенная буква, $ - поиск в конце строки
res28 = re.search(r"^Y....n$", my_string_name)  # Точка - пропущенная буква, ^ - поиск в начале строки
res29 = re.search(r"M.*n", my_string_name)  # Точка и * - пропущенные буквы от M до n

# print(res26[0])
# print(res27[0])
# print(res28)  # None - потому что ^ (начало строки)
# print(res29[0])

# Создание паттерна
my_pattern = re.compile(r"Y....n\.$")
new_pattern = re.compile(r"^M.*\.$")
other_pattern = re.compile(r"Y....n")

# print(my_pattern.search(my_string_name))  # Поиск патерна в строке
# print(new_pattern.match(my_string_name))  # Поиск совпадений патерна в строке
# print(other_pattern.findall(my_string_name))  # Поиск всех элементов в строке и упокование в список


# ---------RE ПРОВЕРКИ

# Проверка почты:
def check_email(email):
    email_regexp = r"[a-zA-Z0-9_.]+@[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+$"
    email_check_pattern = re.compile(email_regexp)  # Создание патерна

    return (email, "valid" if email_check_pattern.fullmatch(email) else "not valid")


check_email("bs@gmail.com")


# Проверка пароля
def check_password(password):
    length_pattern = re.compile(r"\S{8,}")  # Длина не пробельных символов должна быть 8 и более
    lowercase_pattern = re.compile(r"^.*[a-z]+.*$")  # Должна встречаться хотя бы одна маленькая буква (+)
    uppercase_pattern = re.compile(r"^.*[A-Z]+.*$")  # Должна встрчаться хотя бы одна большая буква (+)
    number_pattern = re.compile(r"^.*[0-9]+.*$")  # Должна встрчаться хотя бы одна цифра (+)
    special_symbol_pattern = re.compile(r"^.*[@#$%^&_]+.*$")  # Должен быть хотя бы один спец. символ (+)
    no_whitespace_pattern = re.compile(r"^\S*$")

    if not re.fullmatch(no_whitespace_pattern, password):
        return (False, "No whitespaces allowed in the password")

    if not re.fullmatch(length_pattern, password):
        return (False, "Password must have at least 8 symbols")

    if not re.fullmatch(lowercase_pattern, password):
        return (False, "Password must have at least one lowercase letter")

    if not re.fullmatch(uppercase_pattern, password):
        return (False, "Password must have at least one uppercase letter")

    if not re.fullmatch(number_pattern, password):
        return (False, "Password must have at least one number")

    if not re.fullmatch(special_symbol_pattern, password):
        return (False, "Password must have at least one special symbol (@#$%^&*()!^<>,_+-=)")

    return (True, "Password is valid!")


check_password("sdsdfdDSFS13!&")

# while True:
#     new_pass = input("Please enter password: ")
#     pass_check_result = check_password(new_pass)

#     if pass_check_result[0]:  # True
#         print(pass_check_result[1])
#         break

#     print(pass_check_result[1])

# --------------SQLlite

DB_NAME = "sqlite_db.db"

# Создание новой таблицы
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = """CREATE TABLE IF NOT EXISTS courses (                # Запрос к БД)
#         id integer PRIM KEY,
#         title text NOT NULL,
#         students_qty integer,
#         reviews_qty integer
#     );"""
#     sqlite_conn.execute(sql_request)


courses = [
    (351, "JavaScript course", 415, 100),
    (614, "C++ course", 161, 10),
    (721, "Java full course", 100, 35),
]

# Добавление данных в таблицу
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "INSERT INTO courses VALUES(?, ?, ?, ?)"
#     # sqlite_conn.execute(sql_request, (251, "Python course", 100, 30))  # Запись данных в БД
#     for course in courses:
#         sqlite_conn.execute(sql_request, course)  # Запись данных в БД
#     sqlite_conn.commit()


# Чтение данных с БД
# with sqlite3.connect(DB_NAME) as sqlite_conn:
#     sql_request = "SELECT * FROM courses"  # WHERE reviews_qty>=30
#     sql_cursor = sqlite_conn.execute(sql_request)

#     # for record in sql_cursor: # Вывод всех данных из БД
#     #     print(record)
#     # ИЛИ
#     courses = sql_cursor.fetchall()
#     print(courses)


# ------------ARAY

my_int_array = array("i", [4, 5, 10, 5, 7, 5])
# print(my_int_array)
# print(type(my_int_array))

my_int_array.append(15)
# print(my_int_array)
# print(my_int_array.count(5))

my_int_array.pop()
# print(my_int_array)

# with open("my_array.bin", "wb") as my_file:  # Открытие файла в бинарной записи
# my_int_array.tofile(my_file)  # Запись массива в файл

imported_array = array("i")

# with open("my_array.bin", "rb") as my_file:  # Открытие файла в бинарном чтении
# imported_array.fromfile(my_file, 3)  # Запись файла в массив
# print(imported_array)


# -----------SYS

# print(sys.argv)  # Все аргументы программы

if len(sys.argv) < 3:  # Если аргументов меньше 3
    # raise IOError("You must provide username and password")  # Вывод ошибки
    pass
# username = sys.argv[1]  # Вывод первого аргумента
# password = sys.argv[2]  # Вывод второго аргумента


# ---------------webbrowoser

# webbrowser.open("https://pypi.org") # Открытие сайта


# ---------------pip - package manager for python


# ----------------- EOLYP
# n = input()


# def check_str(data):

#     if "never" not in data.split() or "nobody" not in data.split() or "no" not in data.split():
#         return print("ALL CLEAR")

#     lst = []
#     for char in data.split():
#         if char == "no" or char == "never" or char == "nobody":
#             lst.append(char)

#     for count, elem in sorted(((lst.count(e), e) for e in set(lst)), reverse=True):
#         print(elem)


# check_str(n)

# Jepson no no no no nobody never
# 8 Jepson no no no no nobody never Ashley why ever not Marcus no not never nobody Bazza no never know nobody Hatty why no nobody Hatty nobody never know why nobody Jepson never no nobody Ashley never never nobody no

# ------------------------SMPT
my_email = EmailMessage()

html_template = Template(Path('templates/index.html').read_text())  # Получаем шаблон
html_content = html_template.substitute({'name': 'Yevhen', 'date': 'tommorow'})  # Заменяем переменные в шаблоне

my_email['from'] = 'Yevhen <yp@gmail.com>'
my_email['to'] = 'test@gmail.com'
my_email['subject'] = 'Hello from Python (email with image)'
my_email.set_content(html_content, 'html')  # Заполняем контент в шаблон

with open('images/email.gif', 'rb') as img:  # Отправляем вложение (картинка)
    image_data = img.read()
    my_email.add_attachment(image_data, main_type='image', subtype='gif', filename='email.gif')

with smtplib.SMTP(host='local host', port=2525) as smtp_server:
    smtp_server.ehlo()
    # smtp_server.starttls()
    # smtp_server.login('username', 'password')
    smtp_server.send_message(my_email)  # Отправляем сообщение
    # print('Email was sent!')
# ----------------------------------------


class Figure:
    def __init__(self, coords, width, color) -> None:
        self.coords = coords
        self.width = width
        self.color = color

    def draf(self):
        print(f'Рисование фигуры с кординатами: {self.coords}, с шириной: {self.width}, цветом: {self.color}')


a = Figure((11, 11), 11, 'green')
print(a)

a.draf()


class Point:
    color = 'red'
    circle = 2


print(Point.color)
# Point.color = 'black'
# print(Point.color)
# print(Point.__dict__)

# a = Point()
# b = Point()
# print(a.color)
# print(b.color)
# b.color = 'green'
# print(b.color)
# print(a.__dict__)
# print(b.__dict__)

# print(type(a) == Point)  # Тип a == Point


Point.type_pt = 'disc'
setattr(Point, 'prop', 1)
setattr(Point, 'prop', 'square')  # Классу Point даем атрибут 'prop' со значением 'square'
print(Point.circle)  # Обращение к атирбуту класса
print(Point.__dict__)

print(getattr(Point, 'a', False))  # Получаем атирбут а, если атрибута нет - ворзащается False

del Point.prop  # Удаление атрибута (который точно есть)
print(Point.__dict__)  # Показывает все атрибуты класса
print(hasattr(Point, 'prop'))  # Проверяет, есть ли указанный атрибут в классе

delattr(Point, 'type_pt')  # Удаляем атрибут
print(Point.__dict__)  # Показывает все атрибуты класса

a = Point()
a.x = 1
a.y = 2

b = Point()
b.x = 10
b.y = 20

print(a.__dict__)
print(b.__dict__)

print(Point.__doc__)  # Получаем док класс (описание)

# -------------------------------------------------------------------


class Point:
    color = 'red'
    circle = 2

    def set_cords(self, x, y):
        self.x = x
        self.y = y

        print(f'Вызов метода set_cords для {self}')

    def get_cords(self):
        return f'OBJ: {self} - {(self.x, self.y)}'


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

# -------------------------------------------------


class Point:
    color = 'red'
    circle = 2

    def __init__(self, x=0, y=0) -> None:
        print(f'Вызов метода __init__ для {self}')
        self.x = x
        self.y = y

    def __del__(self):
        print(f'Удаление экземпляра: {str(self)} ')

    def set_cords(self, x, y):
        print(f'Вызов метода set_cords для {self}')
        self.x = x
        self.y = y

    def get_cords(self):
        return f'OBJ: {self} - {(self.x, self.y)}'


pt = Point(10, 20)
# pt.set_cords(1, 2)
print(pt.get_cords())
print(pt.__dict__)

# Суть магического (дандер) метода __init__ заключается в том, чтобы при создании экзампляра класса нужно было СРАЗУ указать необходимые агрументы (в нашем случае координаты). Так же, в данном методе можно указать значение по умолчанию (в параметрах метода).

# Метод __del__ дает возможность задать логику, которая будет отрабаывать ПЕРЕД удалением обьекта, а после обьект будет удален. Другими словами, __del__ отрабаывает без определения, но если его определить - имеем возможность прописать логику перед удалением.

# ---------------------------------------------------------


class Point():
    def __new__(cls, *args, **kwargs):
        print(f"Вызов __new__ для {str(cls)}")

        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print(f"Вызов __init__ для {str(self)}")
        self.x = x
        self.y = y


pt = Point(1, 2)
print(pt)


class DataBase:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)

        return cls.__instance

    def __del__(self):
        DataBase.__instance = None

    def __init__(self, user, psw, port) -> None:
        self.user = user
        self.psw = psw
        self.port = port

    def connect(self):
        print(f'Соединение с БД: {self.user}, {self.psw}, {self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'Запись в БД')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2', '5678', 40)

print(id(db), id(db2))

db.connect()
db2.connect()


# ---------------------------------------------------------


def decorator_function(original_fn):
    def wrapper_function(*args, **kwargs):

        result = original_fn(*args, **kwargs)

        return result

    return wrapper_function


@decorator_function
def my_function(a, b):
    print('Test in my_function')

    return (a, b)


my_function(100, 50)


def outer(a=1):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            return result

        return wrapper

    return decorator


@decorator(123)
def some():
    pass


def new():
    pass


new = decorator(new)


name = "Test"
other_name = "Mike"

name = other_name

other_name = "another"
print(name)
print(other_name)

age = 21
print(id(age))

age += 1
print(age)
print(id(age))

a = []

print(a.)


lst = [1, 2]
print(id(lst))

lst.append(3)
print(id(lst))

dct = {"name": "Jack", "new": "new"}
print(dct[1])
print(id(dct))

dct["name"] = "Another"
print(dct)
print(id(dct))

dct["new"] = "new"

print(dct)
print(id(dct))
print(dct.keys())
print(dct.values())

dct_to_lst = list(dct.values())
print(dct_to_lst)
print(type(dct_to_lst))
