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
import pygame
from components.object import Object
from random import random
import math

class Board():
    def __init__(self, x, y, w, h):
        super().__init__()

        self.game_matrix = []
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.gameDisplay = pygame.display.get_surface()

    def generate_board(self, rows, cols, pad_x = 16, pad_y = 16):
        w = (self.w // cols) - pad_x
        h = (self.h // rows) - pad_y

        row_entries = []
        for _ in range(cols):
            row_entries.append(1 + math.floor(random() * (cols - 1)))
        row_entries[0] = cols

        for i in range(rows):
            self.game_matrix.append([])
            y = self.y + (h + pad_y) * i
            for j in range(row_entries[i]):
                x = self.x + (w + pad_x) * j
                o = Object(x, y, w, h)
                self.game_matrix[i].append(o)

    def update(self):
        for row in self.game_matrix:
            for o in row:
                o.update()
