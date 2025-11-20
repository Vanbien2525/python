# 7. Trò chơi đoán số bí mật
import random

rand = random.randint(1, 100)
print(rand)
while True:
    guess = int(input("Doan so: "))
    if guess == rand:
        print("Chuc mung da doan dung!")
        break
    else:
        print("Chuc may man! Doan lai!!")