class My_Iter:
    def __init__(self, data) -> None:
        self.data = data
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.data):
            raise StopIteration
        value = self.data[self.index]
        self.index += 1
        return value


my_iter = My_Iter([1, 2, 2, 2])

for item in my_iter:
    print(item)


def covert_text_title(string):
    yield [strin.upper() for strin in string]


for my_str in covert_text_title('hool'):
    print(my_str)
