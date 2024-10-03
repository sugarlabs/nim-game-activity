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


def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    help_img = config.images["label"]["help"]
    help_rect = help_img.get_rect()
    if vw(100) / vh(100) > help_rect.width / help_rect.height:
        help_img = utils.scale_image_maintain_ratio(help_img, h=vh(95))
    else:
        help_img = utils.scale_image_maintain_ratio(help_img, w=vw(95))

    theory_btn = Button(vw(80), vh(80), "Show Theory", w=vw(18), h=vh(7))
    back_btn = Button(vw(80), vh(90), "Back to Game", w=vw(18), h=vh(7))

    theory_btn.on_click = lambda: game.set_screen(theory.view)
    back_btn.on_click = lambda: game.set_screen(gamescreen.view)

    buttons.append(back_btn)
    buttons.append(theory_btn)

    def update():
        game.blit_centred(help_img, vw(50), vh(50))
        for btn in buttons:
            btn.update()

    game.update_function = update
