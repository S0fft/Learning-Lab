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
