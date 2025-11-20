# ✅ 9. Nhập chuỗi và đếm chữ 'a'
text = input("Nhap text: ")
count = 0
for ch in text:
    if ch == "a":
        count += 1

print(f"co {count} chu a trong text")