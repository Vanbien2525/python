text = input("Nhap Text: ")
alpha = 0
digit = 0
for c in text:
    if c.isalpha():
        alpha += 1
    elif c.isdigit():
        digit += 1
print("Số chữ cái:", alpha)
print("Số chữ số:", digit)