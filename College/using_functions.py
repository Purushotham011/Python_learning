# x=int(input("enter the value of x : "))
# y=int(input("enter the value of y : "))

# def add(a,b):
#     return a+b
# def subtract(a,b):
#     return a-b
# def multiply(a,b):
#     return a*b
# def divide(a,b):
#     return a/b

# print(f"X + Y = {add(x,y)}")
# print(f"X - Y = {subtract(x,y)}")
# print(f"X * Y = {multiply(x,y)}")
# print(f"X / Y = {divide(x,y)}")

def add(*y,x):
    z=0
    for i in y:
        z=z+i
    return z

print(add(10,20,30,x=40))

x = lambda x,y:x-y
print(x(20,19))