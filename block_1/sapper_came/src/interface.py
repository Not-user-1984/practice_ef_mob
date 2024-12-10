from .game_pole import GamePole


class Interface:
    """
    Класс Interface управляет взаимодействием с пользователем в игре "Сапер".
    Он позволяет запускать игру, вводить координаты клеток,
    открывать их и проверять победу.
    """

    def __init__(self, N, M):
        """
        Инициализирует игровое поле размером N x N с M минами.

        :param N: Размер игрового поля (N x N).
        :param M: Количество мин на поле.
        """
        self.game_pole = GamePole(N, M)

    def run(self):
        """
        Запускает игру. Позволяет пользователю вводить координаты клеток,
        открывать их и проверять победу.
        Игра продолжается до победы или поражения.
        """
        print("Добро пожаловать в игру 'Сапер'!")
        print("""
    Правила игры:
    1. Вы должны открыть все клетки, не содержащие мин.
    2. Если вы откроете клетку с миной, игра заканчивается.
    3. Если вы откроете все клетки без мин, вы выиграете.
    4. Введите координаты клетки в формате 'строка столбец' (например, '0 0').
    5. Чтобы завершить игру, нажмите Ctrl+C или введите 'exit'/'выход'.
    Удачи!
        """)

        start_game = input("Готовы начать игру? (да/нет): ").strip().lower()
        if start_game not in ["да", "yes", "y", "д", "lf"]:
            print("Игра завершена.")
            return

        # Основной цикл игры
        while True:
            self.game_pole.show()
            try:
                user_input = input(
                    "Введите координаты (строка и столбец, например, 0 0): "
                    ).strip()
                if user_input.lower() in ["exit", "выход"]:
                    print("Игра завершена.")
                    break
                i, j = map(int, user_input.split())
                self.game_pole.open_cell(i, j)
                if self.game_pole.check_win():
                    self.game_pole.show()
                    print("Поздравляем! Вы выиграли!")
                    break
            except ValueError:
                print(
                    "Неверный ввод. Пожалуйста, введите два целых числа, разделенных пробелом."
                    )
            except KeyboardInterrupt:
                print("\nИгра прервана.")
                break