#Tao list
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