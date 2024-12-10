class Cell:
    """
    Класс Cell представляет отдельную клетку игрового поля в игре "Сапер".

    Атрибуты:
        around_mines (int): Количество мин вокруг данной клетки. По умолчанию 0.
        mine (bool): Флаг, указывающий, содержит ли клетка мину. По умолчанию False.
        fl_open (bool): Флаг, указывающий, открыта ли клетка. По умолчанию False.
    """

    def __init__(self, around_mines=0, mine=False):
        """
        Инициализирует объект клетки.

        :param around_mines: Количество мин вокруг клетки (по умолчанию 0).
        :type around_mines: int
        :param mine: Указывает, содержит ли клетка мину (по умолчанию False).
        :type mine: bool
        """
        self.around_mines = around_mines
        self.mine = mine
        self.fl_open = False
