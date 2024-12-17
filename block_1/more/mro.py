# class A:
#     def method(self):
#         print("A")

# class B(A):
#     def method(self):
#         print("B")

# class C(A):
#     def method(self):
#         print("C")

# class D(B, C):
#     pass

# d = D()
# d.method()
# Метод из класса B, так как порядок MRO для класса D будет следующим


# # Ромбовидное наследование (Diamond Problem)
# class A:
#     def method(self):
#         print("A")


# class B(A):
#     def method(self):
#         print("B")


# class C(A):
#     def method(self):
#         print("C")


# class D(B, C):
#     pass


# d = D()
# d.method()

def f(a, *args, **kwargs):
    print(a, args, kwargs)

f(1, 2, 3, x=4, y=5)

is_even=lambda x: x % 2 == 0
x, y=y, x
a=31


def fun(arg=1):
    pass
