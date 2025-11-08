#Tao list
# -co thu tu, co the thay doi, co phan tu trung lap
int_number = [1, 5, 7, -87, 10, 65]
print(int_number)
print(type(int_number))

float_number = [1.2, 2.3, 8.5, 6.4, 7]
print(float_number)
print(type(float_number))

friend = ["VBien", "VMinh", "VHau", "TLong", "Khy"]
print(friend)
print(type(friend))
print("-" *40)

#Truy cap gtri trong list
print(f"gia tri thu nhat trong list {int_number} la {int_number[0]}")
print(f"gia tri thu nhat trong list {float_number} la {float_number[2]}")
print(f"gia tri thu nhat trong list {friend} la {friend[3]}")
print("-" *40)

#thay doi gia tri trong list
int_number[0] = 100
print(int_number)
print("-" *40)

#lay chieu dai cua list
print("so luong gia tri cua int_number la:", len(int_number))
print()

#Them gia tri vao list
print("Ban dau:", friend)
friend.append("Duong")
print("Sau do:", friend)
print()

#Xoa gia tri trong list
print("Ban dau:", friend)
friend.remove("Khy")
print("Sau do:", friend)
print()

#Mo rong list bang listkhac
print("Ban dau:", friend)
friend.extend(["Anh", "Chi", "Em"])
print("Sau do:", friend)
print()

print(friend[-7:-5])
print()
print(friend[2:5])
print()


#duyet list
for x in friend:
    print(x)
print()

x = "VBien" in friend
if(x == True):
    print("VBien Co ten trong list")
else:
    print("Khong co ten trong list")
print()

fruits = ["apple", "banana", "guava"]
listCopy1 = fruits
listCopy2 = fruits.copy()
fruits.append("kiwi") # thay doi list ban dau
print("Bi thay doi theo list ban dau: ", listCopy1)
print("Khong bi thay doi theo list ban dau:", listCopy2)

friends = [["Jen", 23], ["Bob", 32], ["Kenny", 37]]
print(type(friends))
print(friends[2][0])

# Ví dụ
# Đánh chỉ số cho list (danh sách)
# Chỉ số trong list đếm từ 0
#          0   1    2   3    4    5
#         -6  -5   -4  -3   -2   -1   
numbers = [1, 10, -23, 45, -89, 1000]

# Lấy ra 3 giá trị đầu tiên từ numbers
# không lấy giá trị tại ví trị 3 (hay vị trí thứ 4)
new_numbers = numbers[0:3:1]
print(new_numbers)

# Copy ra thành một danh sách mới sử dụng list slicing
new_numbers = numbers[:]
print("Hai danh sách có phải là 1 không ?", new_numbers is numbers)
print("Hai danh sách có giá trị bằng nhau không ?", new_numbers == numbers)

print(new_numbers)

s = 0
for i in range(1, 10):
    s+=i
print(s)

#insert item
thislist = ["apple", "banana", "cherry"]
thislist.insert(2, "watermelon")
print(thislist)

#pop xoa chi dinh index
thislist.pop(1)
print(thislist)

#del
thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)
del thislist #xoa thislist

#clear xoa item
thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)

# duyet list while
thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

#syntax
#newlist = [expression for item in iterable if condition == True]
fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)  

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

#sort tang dan
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

#sort giam dan
thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

#sort khoang cach tu 50
def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)

#sort khong phan biet chu HOA hay thuong
thislist = ["Banana", "Orange", "kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)

#reverse dao nguoc list
thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)
