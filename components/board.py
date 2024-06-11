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
        self.gameDisplay = pygame.display.get_surface()

        self.game_matrix = []
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def generate_board(self, rows, cols, pad_x = 16, pad_y = 16):
        self.game_matrix = []
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
                o.on_click = lambda i=i, j=j: self.player_move(i, j)
                self.game_matrix[i].append(o)

    def eliminate_objects(self, row, index):
            self.game_matrix[row] = self.game_matrix[row][:index]

    def game_over_check(self, turn):
            over = True
            for row in self.game_matrix:
                if len(row) != 0:
                     over = False
            if not over:
                 return False
            
            if turn == 0:
                 print("Player Won")
            if turn == 1:
                 print("Robott Won")
            return True

    def player_move(self, row, index):
            self.eliminate_objects(row, index)
            if not self.game_over_check(0):
                self.ai_move()

    def ai_move(self):
        if config.difficulty == 0:
            row = math.floor(random() * len(self.game_matrix))
            while not(len(self.game_matrix[row]) > 0):
                row = math.floor(random() * len(self.game_matrix))
            index = math.floor(random() * len(self.game_matrix[row]))
            self.eliminate_objects(row, index)
        
        self.game_over_check(1)

    def update(self):
        for row in self.game_matrix:
            for o in row:
                o.update()
