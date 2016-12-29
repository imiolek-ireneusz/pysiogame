# -*- coding: utf-8 -*-

import random

import classes.board
import classes.extras as ex
import classes.game_driver as gd
import classes.level_controller as lc


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.level = lc.Level(self, mainloop, 10, 15)
        gd.BoardGame.__init__(self, mainloop, speaker, config, screen_w, screen_h, 11, 6)

    def create_game_objects(self, level=1):
        self.board.draw_grid = False
        self.allow_unit_animations = False
        self.vis_buttons = [1, 1, 1, 1, 1, 1, 1, 1, 0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        self.allow_teleport = False
        s = random.randrange(100, 150, 5)
        v = random.randrange(230, 255, 5)
        h = random.randrange(0, 255, 5)
        color0 = ex.hsv_to_rgb(h, 40, 230)  # highlight 1
        font_color = ex.hsv_to_rgb(h, 255, 140)

        if self.level.lvl == 1:
            data = [11, 6, 3, 9, 2, 1]
        elif self.level.lvl == 2:
            data = [11, 6, 3, 20, 2, 2]
        elif self.level.lvl == 3:
            data = [11, 6, 3, 99, 2, 2]
        elif self.level.lvl == 4:
            data = [11, 6, 5, 9, 3, 1]
        elif self.level.lvl == 5:
            data = [11, 6, 5, 20, 3, 2]
        elif self.level.lvl == 6:
            data = [11, 6, 5, 99, 3, 2]
        elif self.level.lvl == 7:
            data = [11, 6, 7, 9, 4, 1]
        elif self.level.lvl == 8:
            data = [11, 6, 7, 20, 4, 2]
        elif self.level.lvl == 9:
            data = [11, 6, 7, 99, 4, 2]
        elif self.level.lvl == 10:
            data = [11, 6, 9, 9, 5, 1]
        elif self.level.lvl == 11:
            data = [11, 6, 9, 20, 5, 2]
        elif self.level.lvl == 12:
            data = [11, 6, 9, 99, 5, 2]
        elif self.level.lvl == 13:
            data = [11, 6, 11, 9, 6, 2]
        elif self.level.lvl == 14:
            data = [11, 6, 11, 20, 6, 2]
        elif self.level.lvl == 15:
            data = [11, 6, 11, 999, 6, 4]
        self.points = data[4] - 1
        self.chapters = [1, 4, 7, 10, 13, 15]
        self.data = data
        self.layout.update_layout(data[0], data[1])
        self.board.level_start(data[0], data[1], self.layout.scale)

        self.num_list = []

        choice_list = [x for x in range(data[3])]
        for i in range(data[4]):
            index = random.randrange(0, len(choice_list))
            self.num_list.append(choice_list[index])

        color = ((255, 255, 255))

        # create table to store 'binary' solution
        self.solution_grid = [0 for x in range(data[0])]
        self.expression = [" " for x in range(data[0])]

        # find position of first door square
        xd = (data[0] - data[2]) // 2

        # add objects to the board
        h = random.randrange(0, 255, 5)
        number_color = ex.hsv_to_rgb(h, s, v)  # highlight 1
        for i in range(0, data[4]):
            x2 = xd + i * 2
            caption = str(self.num_list[i])
            self.board.add_unit(x2, 2, 1, 1, classes.board.Label, caption, number_color, "", data[5])
            self.solution_grid[x2] = 1
            self.expression[x2] = str(self.num_list[i])
            if i < data[4] - 1:
                self.solution_grid[x2 + 1] = 1
        h = random.randrange(0, 255, 5)
        number_color = ex.hsv_to_rgb(h, s, v)  # highlight 1

        indu = len(self.board.units)
        inds = len(self.board.ships)
        for i in range(0, data[4] - 1):
            self.board.add_unit(xd + i * 2 + 1, 1, 1, 3, classes.board.Letter, [">", "=", "<"], number_color, "",
                                data[5])
            self.board.add_door(xd + i * 2 + 1, 2, 1, 1, classes.board.Door, "", color, "")
            self.board.units[indu + i].door_outline = True
            self.board.ships[inds + i].readable = False
            self.board.all_sprites_list.move_to_front(self.board.units[indu + i])

        instruction = self.d["Drag the slider"]
        self.board.add_unit(0, 5, 11, 1, classes.board.Letter, instruction, color0, "", 7)
        self.board.ships[-1].immobilize()
        self.board.ships[-1].font_color = font_color

        self.board.ships[-1].speaker_val = self.dp["Drag the slider"]
        self.board.ships[-1].speaker_val_update = False
        self.changed_since_check = True  # to make it possible to confirm if numbers are equal
        self.outline_all(0, 1)

    def handle(self, event):
        gd.BoardGame.handle(self, event)  # send event handling up

    def update(self, game):
        game.fill((255, 255, 255))
        gd.BoardGame.update(self, game)  # rest of painting done by parent

    def check_result(self):
        for i in range(len(self.board.ships) - 1):
            # calculate the active value based on grid_y of the slider
            value = self.board.ships[i].value[2 - self.board.ships[i].grid_y]
            if value == "=":
                value = "=="
            self.expression[self.board.ships[i].grid_x] = value
        eval_string = ''.join(self.expression)
        eval_string.strip()
        if eval(eval_string) == True:
            # self.update_score(self.points)
            self.level.next_board()
        else:
            if self.points > 0:
                self.points -= 1
            self.level.try_again()
