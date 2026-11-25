'''
#List[],easy
#append
list=[1,2,3,4]
list.append(5)
print(list)
#extend
a=[4,3,2,1]
a.extend([6,5,7,8])
print(a)
#insert
a.insert(0,10)
print(a)
#remove
a.remove(5)
print(a)
#pop
a.pop()
print(a)#clear
a.clear()
print(a)

#medium
list=["apple","banana","cherry","dragon fruit"]
print(list.index("banana"))
print(list.count("apple"))
list.sort()
print(list)
list.sort(reverse=True)
print(list)
list.extend(["goa","mango"])
print(list)



'''
'''
#Tuple()
#count
a=(1,1,2,3,4,4,5,1)
print(a)
print(a.count(1))
#index
print(a.index(1))
#display
print("first",a[0])
print("middle",a[len(a)//2])
print("last",a[-1])
#reverse
print(a[::-1])

#medium
b=(6,7,8,9)
print((a,b))
result=b*3
print(result)


a=(1,2,3,4)
b=(4,5,6,7)
for i in a:
    if i in b:
        print(i)

a=(10,34,45,7)
even=()
odd=()
for i in a:
    if i%2==0:
        even=even+(i,)
    else:
        odd=odd+(i,)
        print("even:",even)
        print("odd:",odd)
'''
'''
#Set
#add
a={4,5,2,9,8,3,4}
a.add(7)
print(a)
#update
a.update({1,2,3})
print(a)
#remove
a.remove(2)
print(a)
#discard
a.discard(3)
print(a)
#pop
a.pop()
print(a)
#clear
a.clear()
print(a)

a={12,34,21,45}
b={10,12,34,56}
print(a.union(b))
print(a.intersection(b))
print(a.difference(b))
print(a.symmetric_difference(b))
print(a.issubset(b))
print(a.issuperset(b))
print(a.isdisjoint(b))
'''
'''
#Dictionary
s={1:"keerthi",2:"nila",3:"gojo"}
print(s.get(1))
print(s.keys())
print(s.values())
print(s.items())
s.update({4:"kamatchi"})
print(s)
s.update({4:"keeki"})
print(s)
'''
s={1:"keerthi",2:"nila",3:"gojo"}
print(s.pop(2))
print(s)
print(s.popitem())
print(s)
s.update({5:"karthick"})
print(s)
s1=s.copy()
print(s1)

