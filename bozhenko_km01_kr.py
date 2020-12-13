def func(n):
    i = 0
    l = list()
    while i <= n:
        if i % 3 == 0:
            l.extend("Fizz ")
        elif i % 5 == 0:
            l.extend("Buzz ")
        elif i % 15 == 0:
            l.extend("FizzBuzz ")
        else:
            l.extend((str(i) + " "))
        i += 1
    l = "".join(l)
    return l
def f(n):
    i = 1
    while i <= n:
        if i % 5 == 0 and i % 3 == 0:
            print("DixxBuzz ", end = "")
        elif i % 5 == 0:
            print("Dixx ", end = "")
        elif i % 3 == 0:
            print("Buzz ", end = "")
        else:
            print(str(i), " ", end = "")
        i += 1
    return i
    
print(f(16))
    
