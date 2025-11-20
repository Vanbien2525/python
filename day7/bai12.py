"""
Đếm xem trong 10 số nhập vào có bao nhiêu số âm, bao nhiêu số dương
"""
soAm = 0
soDuong = 0

for i in range(10):
    inp = int(input("Nhap so thu " + str(i + 1) + ": "))
    if inp < 0:
        soAm += 1
    else:
        soDuong += 1

print(f"Co {soAm} so am")
print(f"Co {soDuong} so duong")
