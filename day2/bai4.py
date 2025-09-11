# Bài 4: Điểm trung bình và xếp loại

# Nhập vào điểm 3 môn: Toán, Lý, Hóa.

# Tính điểm trung bình.

# Kiểm tra nếu điểm trung bình >= 8 thì in "Giỏi",
# nếu từ 6.5 đến < 8 thì in "Khá",
# nếu từ 5 đến < 6.5 thì in "Trung bình",
# còn lại in "Yếu".

Toan = float(input("Nhập điểm Toán: "))
Ly = float(input("Nhập điểm Lý: "))
Hoa = float(input("Nhập điểm Hóa: "))

avg = (Toan + Ly + Hoa) / 3
print("Điểm trung bình =", avg)

if avg >= 8:
    print("Xếp loại: Giỏi")
elif avg >= 6.5:
    print("Xếp loại: Khá")
elif avg >= 5:
    print("Xếp loại: Trung bình")
else:
    print("Xếp loại: Yếu")
