from repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def get_all_users(self):
        """Получить всех пользователей."""
        return self.repository.get_all()

    def get_user_by_id(self, user_id):
        """Получить пользователя по ID."""
        return self.repository.get_by_id(user_id)

    def create_user(self, user_data):
        """Создать нового пользователя с проверкой уникальности email."""
        # Проверяем, что email уникален
        if self._is_email_unique(user_data["email"]):
            return self.repository.create(user_data)
        raise ValueError("Email already exists")

    def update_user(self, user_id, user_data):
        """Обновить данные пользователя."""
        # Проверяем, что email уникален, если он изменяется
        if "email" in user_data:
            if self._is_email_unique(user_data["email"], user_id):
                return self.repository.update(user_id, user_data)
            raise ValueError("Email already exists")
        return self.repository.update(user_id, user_data)

    def delete_user(self, user_id):
        """Удалить пользователя."""
        return self.repository.delete(user_id)

    def _is_email_unique(self, email, exclude_id=None):
        """Проверяем, что email уникален."""
        users = self.repository.get_all()
        for user in users:
            if user["email"] == email and user["id"] != exclude_id:
                return False
        return True
