from models import Game, Human, Bot
import user_interface as ui
import random

game: Game = None


def run():
    """Запускает основной цикл окна"""

    ui.xo.mainloop()


def start_game(name):
    """Запускает сеанс игры"""

    human = Human(random.choice((ui.X, ui.O)))
    bot = Bot(human.opponent_mark)
    global game
    game = Game(human, bot)
    ui.update_dashboard(name)
    game.start_game(name)
    ui.update_buttons(game.get_game_field())


def get_move(move):
    """Обрабатывает ход"""

    if game and game.game_on and game.human.move(game.get_game_field(), move):
        ui.update_buttons(game.get_game_field())
        if win_combination := game.check_winner(game.human):
            ui.highlight_winner(game.human.mark, win_combination)
            ui.announce_winner(game.human.name)
            game.game_on = False
        elif game.check_draw():
            ui.announce_winner('ничья')
            game.game_on = False
        else:
            game.bot.move(game.get_game_field())
            ui.update_buttons(game.get_game_field())
            if win_combination := game.check_winner(game.bot):
                ui.highlight_winner(game.bot.mark, win_combination)
                ui.announce_winner()
                game.game_on = False
            elif game.check_draw():
                ui.announce_winner('ничья')
                game.game_on = False
