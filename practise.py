# Write a Python script to perform arithmetic operations.Write a Python script to perform arithmetic operations
# 1
a=50
b=30
c=a+b,a-b,a*b,a%b,a/b,a**b,a//b
print(c)

# 2
# Create a list, tuple, and dictionary, and perform basic operations
# list
l1=[1,2,3,4,5,]
l2=[6,7,8,9,10]
print(l1)
print(l1+l2)
print(l1*5)
print(l1[1:6])
print(3 in l1)
print(9 not in l1)
print(max(l1))
print(min(l1))
print(len(l1))
print(type(l1))
l1.append(6)
print(l1)
l1.extend([2,3,4,5,6])
print(l1)
l1.insert(1,8)
print(l1)
del l1[1:3]
print(l1)
l1.pop(3)
print(l1)
l1.remove(1)
print(l1)
l1.sort()
print(l1)
l1.reverse()
print(l1)
res=l1.count(6)
print(res)
res=l1.index(4)
print(res)
l2=l1.copy()
print(l2)
l1[2]=8
print(l1)
res=tuple(l1)
print(res)

tuple
t1=(1,2,3,4,5,)
print(t1.count(5))
print(l1.index(4))
print(list(t1))

# dict
d1={
    "name":"jeeva",
    "age":22,
    "place":"bargur"
}
d2={
    "salary":25000
}
print(d1)
d1.setdefault("size",22)
print(d1)
d1.update(d2)
print(d1)
del d1["salary"]
print(d1)
d1.clear()
print(d1)
d1["age"]=35
print(d1)
res=d1.keys()
print(res)
print(d1.values())
print(d1.items())
print(d1.get("name"))