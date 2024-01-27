class student:
    def get_input(self):
        print("_______________________________________")
        self.name = input("Enter your name     : ")
        self.age = int(input("Enter your age       : "))
        self.year = int(input("Enter Passing Year  : "))
        print("_______________________________________")

    def display(self):
        print("_______________________________________")
        print("Name :",self.name)
        print("Age  :",self.age)
        print("Year :",self.year)
        print("_______________________________________")

s = student()
n=int(input("Enter Number of Students : "))
for _ in range(n):
    s.get_input()
    s.display()