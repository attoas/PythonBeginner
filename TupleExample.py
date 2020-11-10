tupleExample = ('Prame','Guide','Yeen')
print (tupleExample)
tupleExample2 = ('Bank','Kay')
tupleExample3 = tupleExample + tupleExample2
print(tupleExample3)
tupleExample4 = tupleExample * 2
print(tupleExample4)
print(tupleExample4[1:3])


tuple1 = ("Alice", "Bob", "Trudy")
print(tuple1[:2])
print(tuple1[1:])
print(tuple1[1:3])
print('Bob' in tuple1)

for i in tuple1:
    print("Hello :", i)