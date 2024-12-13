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


# Ромбовидное наследование (Diamond Problem)
class A:
    def method(self):
        print("A")


class B(A):
    def method(self):
        print("B")


class C(A):
    def method(self):
        print("C")


class D(B, C):
    pass


d = D()
d.method()