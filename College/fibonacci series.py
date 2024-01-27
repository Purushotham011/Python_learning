def fibonacci_series(n):
    s = []
    if n <= 0:
        return s
    elif n == 1:
        s.append(0)
        return s
    else:
        s = [0, 1]
        while len(s) <= n:
            next_term = s[-1] + s[-2] 
            s.append(next_term)
        return s

num = int(input("Enter a Number : "))
print(fibonacci_series(num))
