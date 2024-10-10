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

THEORY_PAGES_COUNT = 2


def view(game):
    vw = game.vw
    vh = game.vh
    theory_content = {"page_surf": None, "current_page": 0}

    def set_theory_page(page_no):
        theory_page = config.images["label"][f"theory_{page_no}"]
        theory_rect = theory_page.get_rect()
        if vw(100) / vh(100) > theory_rect.width / theory_rect.height:
            theory_page = utils.scale_image_maintain_ratio(theory_page,
                                                           h=vh(100))
        else:
            theory_page = utils.scale_image_maintain_ratio(theory_page,
                                                           w=vw(100))
        theory_content["page_surf"] = theory_page
        theory_content["current_page"] = page_no

    prev_btn = Button(vw(10), vh(90),
                      "Previous",
                      w=vw(18), h=vh(7))
    prev_btn.on_click = lambda: set_theory_page(
        theory_content["current_page"] - 1
    )
    next_btn = Button(vw(80), vh(90),
                      "Next",
                      w=vw(18), h=vh(7))
    next_btn.on_click = lambda: set_theory_page(
        theory_content["current_page"] + 1
    )
    close_btn = Button(vw(80), vh(90),
                       "Close", w=vw(18),
                       h=vh(7))
    close_btn.on_click = lambda: game.set_screen(gamescreen.view)

    set_theory_page(1)

    def update():
        game.blit_centred(theory_content["page_surf"], vw(50), vh(50))

        if theory_content["current_page"] < THEORY_PAGES_COUNT:
            next_btn.update()
        else:
            close_btn.update()

        if theory_content["current_page"] > 1:
            prev_btn.update()

    game.update_function = update
