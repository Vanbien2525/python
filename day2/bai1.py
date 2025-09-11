# Nhập vào từ bàn phím hai số thực number1, number2. Hãy in ra tổng, hiệu, tích, thương, chia nguyên, chia lấy dư, lũy thừa của hai số đó
number1 = float(input("Nhap so 1: "))
number2 = float(input("Nhap so 2: "))

sum = number1 + number2
sub = number1 - number2
multiply = number1 * number2
div = number1 / number2
int_div = number1 // number2
mod = number1 % number2
exp = number1 ** number2

print('-' * 20)
# IN KET QUA
print(number1, '+', number2, '=', sum)
print(number1, '-', number2, '=', sub)
print(number1, '*', number2, '=', multiply)
print(number1, '/', number2, '=', div)
print(number1, '//', number2, '=', int_div)
print(number1, '%', number2, '=', mod)
print(number1, '**', number2, '=', exp)

print("a" >"b") # False