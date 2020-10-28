for i in range(5):
    print(i,end="")

#จะได้ผลลัพธ์เป็น
#01234

for i in range(5):
    print(i,end=" ")

#จะได้ผลลัพธ์เป็น
#0 1 2 3 4

for i in range(5):
    print(i,end="-")

#จะได้ผลลัพธ์เป็น
#0-1-2-3-4
print("")
print(range(10))
print(list(range(10)))

MonthStr = ["Mercury", "Venus", "Earth"]
print("Mercury", "Venus", "Earth", sep='-')
print ("Mercury", "Venus", "Earth")
print (MonthStr)
print("One", end=' ')
print("Two", end=' ')
print("Three", end=' ')