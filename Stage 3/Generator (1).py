

# Generator using yield and next() , it loads the element as a single unit 

def numbers():
    yield 1
    yield 2
    yield 3

gen = numbers()

print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3



def calculator():
    total = 0

    while True:
        value = yield total
        total += value

gen = calculator()

print(next(gen))       # Start generator
print(gen.send(10))    # 10
print(gen.send(20))    # 30
print(gen.send(5))     # 35