# Copyright (C) 2024 Spandan Barve
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import config
import utils
import math
from components.board import Board
from components.button import Button

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    board = Board(vw(5), vh(3), vw(90), vh(60))
    board.generate_board(3, 9)

    reset_btn = Button(vw(5), vh(100 - 15), "RESET", vw(20), vh(10), font=config.font.xl)
    reset_btn.on_click = lambda : board.generate_board(3, 9)
    buttons.append(reset_btn)

    def update():
        board.update()
        for btn in buttons:
            btn.update()

    game.update_function = update
