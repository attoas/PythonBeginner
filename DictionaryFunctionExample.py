menuDict = {}
while True:
    menuName = input("Please Enter Menu :")
    if (menuName.lower() == 'exit'):
        break
    else:
        menuPrice = input("Please Enter Price :")
        menuDict[menuName] = menuPrice

print(menuDict)
#print("ปลาทอดราคา :",menuDict['ปลาทอด'])