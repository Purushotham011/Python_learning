class student :
    def __init__(self,name,age,marks):
        self.name = "student"
        self.age = 20
        self.marks = 100
    def display(self) :
        print("Name  : ",self.name)
        print("Age   : ",self.age)
        print("Marks : ",self.marks)

x= student("sain",21,19)
x.display()