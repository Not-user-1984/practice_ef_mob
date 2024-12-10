from dataclasses import dataclass


@dataclass
class Data:
    data: str
    ip: int

    def __repr__(self):
        return f"Data(data='{self.data}', ip={self.ip})"


class Server:
    _ip_counter = 1

    def __init__(self):
        self.ip = Server._ip_counter
        Server._ip_counter += 1
        self.buffer = []
        print(f"Сервер создан с IP: {self.ip}")

    def send_data(self, data):
        print(f"Сервер {self.ip} отправляет данные: {data}")
        router.buffer.append(data)

    def get_data(self):
        data_list = self.buffer.copy()
        self.buffer.clear()
        print(f"Сервер {self.ip} получил данные: {data_list}")
        return data_list

    def get_ip(self):
        return self.ip


class Router:
    def __init__(self):
        self.buffer = []
        self.servers = {}
        print("Роутер создан")

    def link(self, server):
        self.servers[server.get_ip()] = server
        print(f"Сервер {server.get_ip()} подключен к роутеру")

    def unlink(self, server):
        if server.get_ip() in self.servers:
            del self.servers[server.get_ip()]
            print(f"Сервер {server.get_ip()} отключен от роутера")

    def send_data(self):
        print(f"Буфер роутера перед отправкой: {self.buffer}")
        for data in self.buffer:
            if data.ip in self.servers:
                self.servers[data.ip].buffer.append(data)
                print(f"Данные {data} отправлены на сервер {data.ip}")
        self.buffer.clear()
        print(f"Буфер роутера после отправки: {self.buffer}")


def main():
    """
    Основная функция для демонстрации работы локальной сети.
    Создает серверы, роутер, отправляет данные и показывает процесс.
    """
    global router  # Используем глобальную переменную для роутера

    # Создаем роутер
    router = Router()

    # Создаем серверы
    sv1 = Server()
    sv2 = Server()
    sv3 = Server()

    # Присоединяем серверы к роутеру
    router.link(sv1)
    router.link(sv2)
    router.link(sv3)

    # Создаем пакеты данных
    data1 = Data("Привет от sv1", sv2.get_ip())
    data2 = Data("Привет от sv2", sv3.get_ip())

    # Отправляем пакеты данных с серверов
    sv1.send_data(data1)
    sv2.send_data(data2)

    # Роутер отправляет пакеты данных серверам
    router.send_data()

    # Серверы получают данные
    sv2.get_data()
    sv3.get_data()


if __name__ == "__main__":
    main()
