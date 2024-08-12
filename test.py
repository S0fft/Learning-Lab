import copy


class City:
    def __init__(self, name='Kyiv'):
        self.name = name


class Inforamtion:
    def __init__(self, created_date='12.08.24', city=None):
        self.created_date = created_date
        self.city = city if city else City()


class User:
    def __init__(self, name='Name', surname='Surname', age=20, info=None):
        self.name = name
        self.surname = surname
        self.age = age
        self.info = info if info else Inforamtion()

    def __str__(self) -> str:
        return self.name


user_obj = User()
print(user_obj.info.created_date)

user_obj_2 = copy.copy(user_obj)
user_obj_2.info.created_date = 'NEW'

print(user_obj_2.info.created_date)
print(user_obj.info.created_date)

print(user_obj_2.info.city is user_obj.info.city)
print(user_obj_2.info.city == user_obj.info.city)

a: list[int] = [1, 2, 3]

test_brackets = {
    "()": True,
    "{}": True,
    "[]": True,
    "[()]": True,
    "[({})]": True,
    "[({()})]": True,
    "[({([])})]": True,
    "[({([(){{()()(){}}}])})]": True,
    "[]()[)[)": False,
    "[]()()()[][)[)": False,
    "()([][[[[}}}))": False,
    "[": False,
    "(": False,
    "{": False,
    "{{{": False,
    "{{{{{]}{}{{}{{)))": False,
    "[(])}": False,
    "[(])()()}": False,
}


# ---------------------------------------------------


def is_brackets_correct(input_brackets: str) -> bool:
    result: list = []

    if input_brackets.count('(') == input_brackets.count(')'):
        result.append(1)

    if input_brackets.count('[') == input_brackets.count(']'):
        result.append(1)

    if input_brackets.count('{') == input_brackets.count('}'):
        result.append(1)

    return True if len(result) == 3 else False


print(is_brackets_correct('[({([])})]'))
