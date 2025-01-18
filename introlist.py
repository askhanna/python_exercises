items = ["Mo","Sa",1,2.3, True]

print(1 in items)
print(items[3])
print(items.index(2.3))
print(items[2:])
print(len(items))

items.append("Le")
print(items)

items.extend(["Test1","Test2"])
print(items)

items[1] = "Test3"
print(items)

items_num = [2,3,4,5]
items_num.sort()
print(items_num)

items_str = ['test1','test2','Exam3']
print(sorted(items_str,key=str.lower))
print(sorted(items_str))

