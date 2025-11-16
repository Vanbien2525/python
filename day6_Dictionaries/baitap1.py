# Tạo một dictionary tên student lưu:
# name = “Minh”
# age = 12
# → In dictionary ra màn hình

from pprint import pprint

student = {
    "name" : "Minh",
    "age" : "12"
}
pprint(student)
print()

# → In ra “Toyota”.
car = {"brand": "Toyota", "year": 2020}
print(car["brand"])
print()

# Thêm key "age" = 2.
pet = {"name": "Miu"}
pet["age"] = 2
print(pet)
print()

# Sửa price thành 450.
phone = {"brand": "Samsung", "price": 500}
phone.update(price = 450)
print(phone)
print()

# Xóa key "color".
fruit = {"name": "Apple", "color": "Red"}
fruit.pop("color")
print(fruit)
print()

# → In tất cả key : value bằng vòng lặp for.
country = {"VN": "Vietnam", "JP": "Japan", "KR": "Korea"}
for key, value in country.items():
    print(key, value)
print()

# → Kiểm tra xem “science” có trong dict không.
scores = {"math": 8, "english": 9}
if "science" in scores:
    print("YES")
else:
    print("NO")
print()

# → In ra tên của mẹ (mom).
family = {
  "dad": {"name": "Huy", "age": 40},
  "mom": {"name": "Linh", "age": 38}
}
print(family["mom"] ["name"])
print()

# → In theo mẫu:
# s1
# name: Hoa
# score: 9
# s2
# name: Minh
# score: 8
students = {
  "s1": {"name": "Hoa", "score": 9},
  "s2": {"name": "Minh", "score": 8}
}
for key, obj in students.items():
    print(key)
    for keycon, valuecon in obj.items():
        print(keycon + ":", valuecon )