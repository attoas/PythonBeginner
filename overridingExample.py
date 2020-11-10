class Animal():
    def eat(self):
        print("Eating Eating!")

class Cat(Animal):
    __name = ""
    def setName(self, text):
        self.name = text
        print("Setting New Cat Name = ", self.name)
    def eat(self):
        print("Meow !!", self.name)

cat1 = Cat()
cat1.setName("Kitty")
#cat1.__name = "KittyOpened"  #  __name เป็น ตัวแปร ที่ encapsulation ไว้ ผมไม่สามารถ ส่งกำหนดค่าเข้าไปให้มันได้
cat1.eat()
