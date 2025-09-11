# Bài 3: Kiểm tra số chẵn và trong khoảng

# Viết chương trình nhập vào một số nguyên n.

# Kiểm tra xem n có chẵn hay không.

# Kiểm tra xem n có nằm trong khoảng [10, 50] hay không.

n = int(input("Nhập n: "))

print(f"{n} là số chẵn" if n % 2 == 0 else f"{n} là số lẻ")

print(f"{n} nằm trong khoảng 10 và 50" if 10 <= n <= 50 else f"{n} không nằm trong khoảng 10 và 50")
