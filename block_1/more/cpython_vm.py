import dis


def add(a, b):
    return a + b


result = add(3, 5)
print(result)


def add(a, b):
    return a + b


dis.dis(add)