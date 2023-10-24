import user_interface as ui

GRID_SIZE = 9
WIN_COMBS = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
             (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))


class Game:
    def __init__(self, human, bot):
        self.game_field = None
        self.game_on = False
        self.human = human
        self.bot = bot

    def start_game(self, name) -> None:
        """Начинает или перезапускает игру"""
        if name.strip():
            self.game_on = True
            self.game_field = [ui.space] * GRID_SIZE
            self.human.name = name
            if self.bot.mark == ui.X:
                self.bot.move(self.game_field)

    def get_game_field(self) -> list:
        """Возвращает поле"""
        return self.game_field

    def check_draw(self) -> bool:
        """Проверяет текущее положение на ничью"""
        return ui.space not in self.game_field

    def check_winner(self, player) -> tuple or False:
        """Проверяет, не сложилась ли у игрока победная комбинация"""
        for comb in WIN_COMBS:
            if self.game_field[comb[0]] == self.game_field[comb[1]] == self.game_field[comb[2]] == player.mark:
                return comb
        return False


class Player:
    def __init__(self, mark):
        self.mark = mark
        self.opponent_mark = ui.X if self.mark == ui.O else ui.O


class Human(Player):
    def __init__(self, mark, name=None):
        super().__init__(mark)
        self.name = name

    def move(self, game_field: list, move: int) -> bool:
        """Обрабатывает ход игрока, если это возможно"""
        available_cells = [i for i in range(len(game_field)) if game_field[i] == ui.space]
        if move in available_cells:
            game_field[move] = self.mark
            return True
        return False


class Bot(Player):
    def move(self, game_field: list) -> None:
        """Обрабатывает ход бота"""
        if self.get_win_move(game_field, self.mark):
            return
        if self.get_win_move(game_field, self.opponent_mark):
            return
        if game_field[4] == ui.space:
            game_field[4] = self.mark
            return
        for k, v in {0: 8, 2: 6, 6: 2, 8: 0}.items():
            if game_field[k] == self.opponent_mark and game_field[v] == ui.space:
                game_field[v] = self.mark
                return
        for i in (0, 2, 6, 8):
            if game_field[i] == ui.space:
                game_field[i] = self.mark
                return
        for i in (1, 3, 5, 7):
            if game_field[i] == ui.space:
                game_field[i] = self.mark
                return

    def get_win_move(self, field: list, mark_to_check: str) -> bool:
        """Проверяет, может ли игрок выиграть следующим ходом и ставит знак в выигрышную клетку"""
        for comb in WIN_COMBS:
            i, k, j = comb
            if field[i] == ui.space and field[k] == mark_to_check and field[j] == mark_to_check:
                field[i] = self.mark
                return True
            if field[j] == ui.space and field[i] == mark_to_check and field[k] == mark_to_check:
                field[j] = self.mark
                return True
            if field[k] == ui.space and field[j] == mark_to_check and field[i] == mark_to_check:
                field[k] = self.mark
                return True
        return False
