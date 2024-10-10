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

import utils
import config
from components.button import Button
from views import game as gamescreen
from views import theory
import config

DIFFICULTY_OPTIONS = ["Easy", "Medium", "Difficult"]

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    difficulty_text = config.font.lg.render("Difficulty", True, config.front_color)
    difficulty_btn = Button(vw(44), vh(24), DIFFICULTY_OPTIONS[config.difficulty], w=vw(12), h=vh(5), font = config.font.md)
    def difficulty_switch():
        nonlocal difficulty_btn
        config.difficulty = (config.difficulty + 1) % 3
        difficulty_btn = Button(vw(44), vh(24), DIFFICULTY_OPTIONS[config.difficulty], w=vw(12), h=vh(5), font = config.font.md)
        difficulty_btn.on_click = difficulty_switch
    difficulty_btn.on_click = difficulty_switch

    def update():
        game.blit_centred(difficulty_text, vw(50), vh(21))
        difficulty_btn.update()
    game.update_function = update
