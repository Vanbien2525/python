# 5. Nhập 7 số và tìm số lớn nhất
maxx = 0
for i in range(7):
    n = int(input("Nhap so: "))
    if n >= maxx:
        maxx = n
print("so lon nhat la:", maxx)