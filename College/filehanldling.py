# file = open("D:/PythonProjects/758/sain.txt","rb+")
# print(file.read(),end="")

file = open("D:/PythonProjects/758/sain.txt","w+")
for line in file:
    print(line,end='')

print(file.write("Welcome to Alliance."))