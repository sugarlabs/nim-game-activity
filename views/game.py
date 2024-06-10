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


from components.button import Button
from views import game as gamescreen
import config
import utils
import math

def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    # play_button = Button(vw(50), vh(55), "Play", h=vh(20), font=config.font_primary.xl)
    # play_button.on_click = lambda: game.set_screen(gamescreen.view)
    # buttons.append(play_button)

    def update():
        # draw()
        for btn in buttons:
            btn.update()

    game.update_function = update
