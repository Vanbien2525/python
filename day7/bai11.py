"""
🟦 Bài 11 — Tính tổng các số từ 1 → n nhưng bỏ qua số chia hết 4

Ví dụ nhập n = 10
Bỏ: 4, 8
"""
total = 0
n = int(input("Nhap N: "))
for i in range(1, n + 1):
    if i % 4 == 0: continue
    total += i
print(f"Tong cac so tu 1 den {n} la: {total}")