"""
✅ 6. In số 1 → 40 với emoji

🐸 nếu chia hết 3

🐱 nếu chia hết 5

🐸🐱 nếu chia hết cả 3 và 5
"""
for i in range(1, 41):
    if i % 3 == 0 and i % 5 == 0:
        print("🐸🐱")
    elif i % 3 == 0:
        print("🐸")
    elif i % 5 == 0:
        print("🐱")
    else:
        print(i)