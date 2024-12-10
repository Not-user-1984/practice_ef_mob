from flask import Flask, jsonify, request
from services import UserService

app = Flask(__name__)

user_service = UserService()


@app.route('/users', methods=['GET'])
def get_users():
    """Получить всех пользователей."""
    users = user_service.get_all_users()
    return jsonify(users)


@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """Получить пользователя по ID."""
    user = user_service.get_user_by_id(user_id)
    if user:
        return jsonify(user)
    return jsonify({'error': 'User not found'}), 404


@app.route('/users', methods=['POST'])
def create_user():
    """Создать нового пользователя."""
    user_data = request.get_json()
    if not user_data or 'name' not in user_data or 'email' not in user_data:
        return jsonify({'error': 'Invalid data'}), 400
    try:
        user = user_service.create_user(user_data)
        return jsonify(user), 201
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    """Обновить данные пользователя."""
    user_data = request.get_json()
    if not user_data:
        return jsonify({'error': 'Invalid data'}), 400
    try:
        updated_user = user_service.update_user(user_id, user_data)
        if updated_user:
            return jsonify(updated_user)
        return jsonify({'error': 'User not found'}), 404
    except ValueError as e:
        return jsonify({'error': str(e)}), 400


@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):
    """Удалить пользователя."""
    if user_service.delete_user(user_id):
        return jsonify({'message': 'User deleted'})
    return jsonify({'error': 'User not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
