import threading


class Singleton:
    _instance = None
    _lock = None
    _count = 0

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._lock = threading.Lock()
            if cls._instance is None:
                cls._instance = super().__new__(cls)
                cls._count += 1
        return cls._instance

    def __init__(self):
        print(f'Singleton instance created: {self._count}')
        self.value = 'Singleton instance value'


singleton1 = Singleton()
singleton2 = Singleton()

singleton1.value = 'New value for singleton1'
print(singleton1.value)
print(singleton2.value)
print(singleton1 is singleton2)
print(singleton1 is Singleton())
