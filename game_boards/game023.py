# -*- coding: utf-8 -*-

import random
import sys

import classes.board
import classes.extras as ex
import classes.game_driver as gd
import classes.level_controller as lc
import classes.maze_lvls as gl


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.level = lc.Level(self, mainloop, 5, 5)
        gd.BoardGame.__init__(self, mainloop, speaker, config, screen_w, screen_h, 27, 19)

    def create_game_objects(self, level=1):
        self.board.draw_grid = False
        self.vis_buttons = [0, 1, 1, 1, 1, 1, 1, 0, 0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)
        self.allow_unit_animations = False
        self.change_count = 0
        self.allow_teleport = False
        s = random.randrange(150, 205, 5)
        v = random.randrange(150, 205, 5)
        h = random.randrange(0, 255, 5)
        letter_bg = (255, 255, 255)
        letter_font_color = (0, 0, 0)
        # data = [0:x_count, 1:y_count, 2:games_per_level, 3:bug_img, 4:level_maps]
        bug_img = "bug_32.png"
        if self.mainloop.scheme is not None:
            if self.mainloop.scheme.dark:
                bug_img = "bug_32b.png"
                letter_bg = (0, 0, 0)
                s = 100
                v = 50
            h = 40
            letter_font_color = self.mainloop.scheme.u_font_color

        color = ex.hsv_to_rgb(h, s, v)
        color1 = ex.hsv_to_rgb(h, 40, 230)  # label
        color2 = ex.hsv_to_rgb(h, 150, 230)  # completed
        color3 = ex.hsv_to_rgb(h, 255, 230)  # current
        self.clr = [color1, color2, color3]

        if self.level.lvl == 1:  # img_ 32x32
            data = [27, 19, 10, bug_img, 2, gl.lvl1]
        elif self.level.lvl == 2:  # img_ 32x32
            data = [27, 19, 10, bug_img, 3, gl.lvl1]
        elif self.level.lvl == 3:  # img_ 32x32
            data = [27, 19, 10, bug_img, 4, gl.lvl1]
        elif self.level.lvl == 4:  # img_ 32x32
            data = [27, 19, 10, bug_img, 5, gl.lvl1]
        elif self.level.lvl == 5:  # img_ 32x32
            data = [27, 19, 10, bug_img, 6, gl.lvl1]
        self.points = data[4]
        self.data = data

        self.layout.update_layout(data[0], data[1])
        self.board.level_start(data[0], data[1], self.layout.scale)
        self.solution = [data[0] - 2, data[1] - 2]

        letter_table = []
        letter_table.extend(self.lang.alphabet_lc)
        letter_table.extend(self.lang.accents_lc)
        letter_table.extend(self.lang.alphabet_uc)
        letter_table.extend(self.lang.accents_uc)

        self.word = self.lang.di[data[4]][random.randrange(1, self.lang.di[data[4]][0])]
        if sys.version_info < (3, 0):
            self.wordu = unicode(self.word, "utf-8")
            word_len = len(self.wordu)
            self.word_l = []
            # dirty way of replacing the word with letters from alphabet
            for each in self.wordu:
                for i in range(len(letter_table)):
                    if each == unicode(letter_table[i], "utf-8"):
                        self.word_l.append(letter_table[i])
            self.word = self.word_l
            self.s_word = ''.join(self.word_l)
        else:
            word_len = len(self.word)
            self.word_l = self.word
            self.s_word = self.word
            self.word = list(self.word)

        self.word_len = word_len

        self.remaining = self.word_len + 0
        shuffled = self.word[:]
        self.searched_letter = self.word[0]

        board_number = random.randrange(1, data[5][0][0] + 1)

        w = self.word_len
        x = (data[0] - w) // 2
        x2 = data[0] // 2
        midscreen = data[1] // 2
        for i in range(self.word_len):
            if i == 0:
                colr = color3
            else:
                colr = color1
            self.board.add_unit(x + i, midscreen, 1, 1, classes.board.Label, self.word[i], colr, "", 1)
            self.board.units[i].set_outline(0, 3)

        avail = [[[], []], [[], []]]
        for j in range(data[1]):
            for i in range(data[0]):
                if data[5][board_number][j][i] == 1:
                    self.board.add_unit(i, j, 1, 1, classes.board.Obstacle, "", color)
                # create availability table:
                else:
                    if (1 < i < data[0] - 2) and ((1 < j < midscreen - 2) or (midscreen + 2 < j < data[1] - 2)):
                        if i % 4 == 0:
                            # create table 1
                            if j < midscreen - 2:
                                avail[0][0].append([i, j])
                            else:
                                avail[0][1].append([i, j])
                        elif (i + 2) % 4 == 0:
                            # create table 2
                            if j < midscreen - 2:
                                avail[1][0].append([i, j])
                            else:
                                avail[1][1].append([i, j])
        # select positions:
        self.letter_pos = []
        col = [[], []]
        ln = [[len(avail[0][0]), len(avail[0][1])], [len(avail[1][0]), len(avail[1][1])]]
        av1 = random.randrange(0, 2)
        av2 = 0
        for i in range(self.word_len):
            if i > self.word_len // 2: av2 = 1
            not_in = True
            while not_in:
                pos = avail[av1][av2][random.randrange(0, ln[av1][av2])]
                if pos[0] not in col[av2]:
                    not_in = False
                    col[av2].append(pos[0])
                    self.letter_pos.append(pos)
                    self.board.add_door(pos[0], pos[1], 1, 1, classes.board.PickUp, shuffled[i], letter_bg)
                    self.board.units[-1].font_color = letter_font_color
        self.letter_pos2 = self.letter_pos[:]

        # add the bug
        self.board.add_unit(x2, midscreen - 1, 1, 1, classes.board.ImgShipRota, self.s_word, letter_bg, data[3])
        self.board.ships[0].audible = False
        self.board.ships[0].outline = False
        self.board.ships[0].draggable = True
        self.board.all_sprites_list.move_to_front(self.board.ships[0])

        self.ships_count = len(self.board.ships)

        self.board.active_ship = 0
        self.ship_id = 0
        self.units_len = len(self.board.units)
        self.board.moved = self.walk_through
        self.drag = False

    def handle(self, event):
        gd.BoardGame.handle(self, event)  # send event handling up

    def update(self, game):
        game.fill((255, 255, 255))
        gd.BoardGame.update(self, game)  # rest of painting done by parent

    def walk_through(self):
        for i in range(self.word_len):
            if self.board.ships[self.board.active_ship].grid_pos == self.letter_pos[i]:
                if self.word[i] == self.searched_letter:
                    self.remaining -= 1
                    self.letter_pos[i] = [-1, -1]
                    if self.remaining == 0:
                        self.say(self.s_word + ".")
                        # self.update_score(self.points)
                        self.level.next_board()
                    else:
                        self.searched_letter = self.word[self.word_len - self.remaining]
                        # change colors
                        rem = self.word_len - self.remaining
                        self.board.units[rem].color = self.clr[2]
                        self.board.units[rem - 1].color = self.clr[1]
                        self.board.units[rem].set_outline(0, 3)
                        self.board.units[rem - 1].set_outline(0, 1)
                        self.board.units[rem].update_me = True
                        self.board.units[rem - 1].update_me = True
                        for j in range(self.units_len - self.word_len, self.units_len):
                            if self.board.ships[self.board.active_ship].grid_pos == self.board.units[j].grid_pos:
                                self.board.units[j].kill()
                                self.mainloop.redraw_needed[0] = True
                                self.say(self.word[i])
                                break
                    break

                else:
                    self.level.game_over()
                    break

    def after_keydown_move(self):
        pass  # self.walk_through()

    def check_result(self):
        if self.changed_since_check:
            self.walk_through()
