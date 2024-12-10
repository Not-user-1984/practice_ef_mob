# repository.py

class UserRepository:
    def __init__(self):
        self.users = {}
        self.next_id = 1

    def get_all(self):
        """Получить всех пользователей."""
        return list(self.users.values())

    def get_by_id(self, user_id):
        """Получить пользователя по ID."""
        return self.users.get(user_id)

    def create(self, user_data):
        """Создать нового пользователя."""
        user_id = self.next_id
        self.next_id += 1
        user_data['id'] = user_id
        self.users[user_id] = user_data
        return user_data

    def update(self, user_id, user_data):
        """Обновить данные пользователя."""
        if user_id in self.users:
            self.users[user_id].update(user_data)
            return self.users[user_id]
        return None

    def delete(self, user_id):
        """Удалить пользователя."""
        if user_id in self.users:
            del self.users[user_id]
            return True
        return False
