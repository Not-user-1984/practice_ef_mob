

class ObjList:
    def __init__(self, data):
        self.__data = data
        self.__next = None
        self.__prev = None

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def get_data(self):
        return self.__data

    def __str__(self):
        return f'Data: {self.__data}'


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, obj):
        if self.head is None:
            self.head = obj
            self.tail = obj
        else:
            self.tail.set_next(obj)
            obj.set_prev(self.tail)
            self.tail = obj

    def remove(self, obj):
        if self.tail is None:
            return
        if self.tail == self.head:
            self.head = None
            self.tail = None
        else:
            prev_obj = self.tail.get_prev()
            if prev_obj:
                prev_obj.set_next(None)
                self.tail = prev_obj
            self.tail = prev_obj

    def get_data(self):
        data_list = []
        current = self.head
        while current is not None:
            data_list.append(current.get_data())
            current = current.get_next()
        return data_list


lst = LinkedList()
lst.add(ObjList('First'))
lst.add(ObjList('Second'))
lst.add(ObjList('Third'))
res = lst.get_data()

print(res)