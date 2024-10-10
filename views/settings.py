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


def view(game):
    buttons = []
    vw = game.vw
    vh = game.vh

    DIFFICULTY_OPTIONS = ["Easy", "Medium", "Difficult"]
    ROBOTS = list(config.images["robot"].keys())
    OBJECTS = list(config.images["object"].keys())

    difficulty_text = config.font.lg.render("Difficulty", True, config.front_color)
    difficulty_btn = Button(vw(44), vh(24), DIFFICULTY_OPTIONS[config.difficulty], w=vw(12), h=vh(5), font = config.font.md)
    def difficulty_switch():
        nonlocal difficulty_btn
        config.difficulty = (config.difficulty + 1) % 3
        difficulty_btn = Button(vw(44), vh(24), DIFFICULTY_OPTIONS[config.difficulty], w=vw(12), h=vh(5), font = config.font.md)
        difficulty_btn.on_click = difficulty_switch
    difficulty_btn.on_click = difficulty_switch

    prev_robot = ROBOTS.index(config.current_robot)
    config.current_robot = ROBOTS[prev_robot - 1]
    robot_text = config.font.lg.render("Robot", True, config.front_color)
    robot_btn = None
    def robot_switch():
        nonlocal robot_btn
        config.current_robot = ROBOTS[(ROBOTS.index(config.current_robot) + 1) % len(ROBOTS)]
        robot_btn = Button(vw(10), vh(40), "", w=vw(30), h=vh(30), font = config.font.md)
        robot_btn_surf = config.images["robot"][config.current_robot]
        robot_btn_surf = utils.scale_image_maintain_ratio(robot_btn_surf, h=vh(30))
        robot_btn.set_image_rect(robot_btn_surf)
        robot_btn.on_click = robot_switch
    robot_switch()

    prev_object = OBJECTS.index(config.current_object)
    config.current_object = OBJECTS[prev_object - 1]
    object_text = config.font.lg.render("Counter", True, config.front_color)
    object_btn = None
    def object_switch():
        nonlocal object_btn
        config.current_object = OBJECTS[(OBJECTS.index(config.current_object) + 1) % len(OBJECTS)]
        object_btn = Button(vw(71), vh(43), "", w=vw(30), h=vh(30), font = config.font.md)
        object_btn_surf = config.images["object"][config.current_object]
        object_btn_surf = utils.scale_image_maintain_ratio(object_btn_surf, h=vh(25))
        object_btn.set_image_rect(object_btn_surf)
        object_btn.on_click = object_switch
    object_switch()

    back_btn = Button(vw(43), vh(90), "Back to Game", w=vw(16), h=vh(7))
    back_btn.on_click = lambda: game.set_screen(gamescreen.view)

    def update():
        game.blit_centred(difficulty_text, vw(50), vh(21))
        game.blit_centred(robot_text, vw(19), vh(37))
        game.blit_centred(object_text, vw(78), vh(37))

        difficulty_btn.update()
        object_btn.update()
        robot_btn.update()
        back_btn.update()
    game.update_function = update
