# Tuples:
#     -co thu tu, khong the thay doi, co trung lap

thistuple = ("apple", "banana", "cherry")
print(thistuple)
print(type(thistuple))
print(len(thistuple))
print(thistuple[1])
print(thistuple[-1])

# Range of Indexes
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
print(thistuple[2:5])

# Range of Negative Indexes
print(thistuple[-4:-1])

#Change Tuple Values: chuyen tuple -> list, thay doi gia tri, list -> tuple
x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)

#add item
# 1. tuple -> list, list -> tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)
# 2. cong 1 tuple khac vao
thistuple = ("apple", "banana", "cherry")
y = ("kiwi",)
thistuple += y
print(thistuple)

#remove tuple
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)
print(thistuple)
del thistuple

#Unpacking a Tuple(Dong goi)
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)

fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

#Loop Through a Tuple
thistuple = ("apple", "banana", "cherry")
for x in thistuple:
  print(x)

thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])
  
thistuple = ("apple", "banana", "cherry")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i += 1
    
#Join Tuples
tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)
tuple3 = tuple1 + tuple2
print(tuple3)
# *2 tuple
fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple)