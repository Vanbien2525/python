# dict:
#     -Co thu tu
#     -Luu tru theo keo key:value
#     -Khong duoc trung key
#     -value co the trung va bat cu kieu du lieu nao
#     -Co the thay doi
#
from pprint import pprint

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
print(thisdict)

#leng
print(len(thisdict))

thisdict = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(thisdict)
print(type(thisdict))

thisdict = dict(name="John", age=36, country="Norway")
print(thisdict)

# Accessing Items
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict["model"]
print(x)

#get()
x = thisdict.get("model")
print(x)

#keys(): return keys
x = thisdict.keys()
print(x)

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)  #before the change
car["color"] = "white"
print(x)  #after the change

#values(): return value
x = car.values()
print(x)

#items(): return each item in a dictionary, as tuples in a list.
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
x = thisdict.items()
print(x)

#check
if "model" in thisdict:
    print("Yes, 'model' is one of the keys in the thisdict dictionary")

#update()
thisdict.update({"color": "red"})
print(thisdict)

#pop(): method removes the item with the specified key name:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.pop("model")
print(thisdict)

#popitem():method removes the last inserted item
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.popitem()
print(thisdict)

#del keyword removes the item with the specified key name, delete the dictionary completely:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
del thisdict["model"]  # del thisdict
print(thisdict)  # print(thisdict) #this will cause an error because "thisdict" no longer exists.

# clear() method empties the dictionary:
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
thisdict.clear()
print(thisdict)

#Loop Through a Dictionary
thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}
# Duyet key
for x in thisdict:
    print(x)
for x in thisdict.keys():
    print(x)

# Duyet value
for x in thisdict:
    print(thisdict[x])
for x in thisdict.values():
    print(x)

#Loop through both keys and values, by using the items() method:
for x, y in thisdict.items():
    print(x, y)

#Copy a Dictionary
# copy()
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
mydict = thisdict.copy()
print(mydict)

#Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}
pprint(myfamily)

child1 = {
  "name" : "Emil",
  "year" : 2004
}
child2 = {
  "name" : "Tobias",
  "year" : 2007
}
child3 = {
  "name" : "Linus",
  "year" : 2011
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
print()
pprint(myfamily)

#Access Items in Nested Dictionaries
myfamily = {
  "child1" : {
    "name" : "Emil",
    "year" : 2004
  },
  "child2" : {
    "name" : "Tobias",
    "year" : 2007
  },
  "child3" : {
    "name" : "Linus",
    "year" : 2011
  }
}

print(myfamily["child2"]["name"])

#Loop Through Nested Dictionaries
myfamily = {
    "child1": {
        "name": "Emil",
        "year": 2004
    },
    "child2": {
        "name": "Tobias",
        "year": 2007
    },
    "child3": {
        "name": "Linus",
        "year": 2011
    }
}

for x, obj in myfamily.items():
    print(x)
    for y in obj:
        print(y + ':', obj[y])