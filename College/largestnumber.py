#code for finding the largest number using functions

def largest(a,b,c):
    if a>b:
        if a>c:
            return a
        else:
            return c
    else:
        if b>c:
            return b
        else:
            return c
print(largest(1,2,3))

#code for finding the smallest number using functions
def smallest(a,b,c):
    if a<b:
        if a<c:
            return a
        else:
            return c
    else:
        if b<c:
            return b
        else:
            return c
print(smallest(1,2,3))
