
colors = ["red","yellow","blue"]
print(colors)

colors1 = ('red', 'yellow', 'green')
print(colors1)

print(type(colors1))

print(type(colors))


list1 = ["name", 5, True, 3.6, "8"]
print(list1)
print(type(list1))

print(list1[1])
print(list1[-2])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])
print(thislist[:3])

thislist.append("wood-Apple")
print(thislist)
thislist.insert(1, 'apple1')
print(thislist)

thislist.remove("apple")
print(thislist)

thislist.remove(thislist[0])
print(thislist)

newlist = ["apple", "banana", "cherry"]
newlist.pop(0)
print(newlist)