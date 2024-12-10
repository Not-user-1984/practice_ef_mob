import random
from .cell import Cell


class GamePole:
    """
    Класс GamePole управляет игровым полем для игры "Сапер".
    Он отвечает за инициализацию поля, расстановку мин, отображение поля и проверку победы.
    """

    def __init__(self, N, M):
        """
        Инициализирует игровое поле размером N x N с M минами.

        :param N: Размер игрового поля (N x N).
        :param M: Количество мин на поле.
        """
        self.N = N
        self.M = M
        self.pole = [[Cell() for _ in range(N)] for _ in range(N)]
        self.init()

    def init(self):
        """
        Инициализирует поле, расставляя мины случайным образом и вычисляя количество мин вокруг каждой клетки.
        """
        # Расставляем мины случайным образом
        mines = random.sample(range(self.N * self.N), self.M)
        for mine in mines:
            row = mine // self.N
            col = mine % self.N
            self.pole[row][col].mine = True

        # Вычисляем количество мин вокруг каждой клетки
        for i in range(self.N):
            for j in range(self.N):
                if not self.pole[i][j].mine:
                    mines_count = 0
                    for di in range(-1, 2):
                        for dj in range(-1, 2):
                            ni, nj = i + di, j + dj
                            if 0 <= ni < self.N and 0 <= nj < self.N and self.pole[ni][nj].mine:
                                mines_count += 1
                    self.pole[i][j].around_mines = mines_count

    def show(self):
        """
        Отрисовывает игровое поле с нумерацией строк и столбцов.
        """
        # Выводим заголовок с номерами столбцов
        print("   " + " ".join(f"{j:2}" for j in range(self.N)))
        print("  +" + "--" * self.N + "+")

        for i, row in enumerate(self.pole):
            print(f"{i:2}| " + " ".join(['*' if cell.mine and cell.fl_open else 
                                        str(cell.around_mines) if cell.fl_open else '#' 
                                        for cell in row]) + " |")
        print("  +" + "--" * self.N + "+")

    def open_cell(self, i, j):
        """
        Открывает клетку с координатами (i, j).
        Если в клетке находится мина, игра заканчивается.
        Если вокруг клетки нет мин, открываются все соседние клетки.

        :param i: Индекс строки клетки.
        :param j: Индекс столбца клетки.
        """
        if not (0 <= i < self.N and 0 <= j < self.N):
            return
        cell = self.pole[i][j]
        if cell.fl_open:
            return
        cell.fl_open = True
        if cell.mine:
            print("Игра окончена! Вы наткнулись на мину.")
            self.draw_field()
            exit()
        elif cell.around_mines == 0:
            for di in range(-1, 2):
                for dj in range(-1, 2):
                    ni, nj = i + di, j + dj
                    self.open_cell(ni, nj)

    def check_win(self):
        """
        Проверяет, выиграл ли игрок.
        Возвращает True, если все клетки без мин открыты, иначе False.

        :return: True, если игрок выиграл, иначе False.
        """
        for row in self.pole:
            for cell in row:
                if not cell.mine and not cell.fl_open:
                    return False
        return True
