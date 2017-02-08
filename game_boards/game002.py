# -*- coding: utf-8 -*-

import pygame

import classes.board
import classes.game_driver as gd
import classes.level_controller as lc


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config, screen_w, screen_h):
        self.level = lc.Level(self, mainloop, 1, 1)
        gd.BoardGame.__init__(self, mainloop, speaker, config, screen_w, screen_h, 11, 10)

    def create_game_objects(self, level=1):
        self.board.draw_grid = False
        self.show_info_btn = False

        color1 = (220, 220, 220)
        color2 = (255, 255, 255)

        font_color = (40, 40, 40)
        data = [18, 12]
        # stretch width to fit the screen size
        x_count = self.get_x_count(data[1], even=True)
        if x_count > data[0]:
            data[0] = x_count

        self.data = data

        self.vis_buttons = [0, 0, 0, 0, 1, 0, 1, 0, 0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)

        self.layout.update_layout(data[0], data[1])
        scale = self.layout.scale
        self.board.level_start(data[0], data[1], scale)

        self.board.board_bg.line_color = (200, 200, 200)
        if self.mainloop.scheme is not None:
            self.board.board_bg.line_color = self.mainloop.scheme.u_line_color
        self.board.board_bg.update_me = True

        middle = self.data[0] // 2
        lang_width = 2
        credits_width = (self.data[0] // 2) - lang_width

        # if there's enough space extend the language width by 1
        # the 7 below is hardcoded based on current length of text, may need adjusting if longer credits text added
        if credits_width > 7:
            lang_width = 3
            credits_width -= 1

        left = 0
        colors = [color1, color2]

        self.board.add_unit(0, 0, data[0], 1, classes.board.Label, self.lang.d["Translators"], colors[1], "", 4)

        # column 1
        top = 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Catalan", "Català"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            ["Guillem Jover", "http://www.hadrons.org/~guillem/"], colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(0, top, lang_width, 1, classes.board.Label, ["English", "English"], colors[top % 2], "", 6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            ["Kamila Roszak-Imiolek", "Ireneusz Imiolek"],
                            colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Finnish", "Suomalainen"], colors[top % 2],
                            "", 6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label, ["Aapo Rantalainen"],
                            colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["French", "Français"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            ["Gino Ingras", "edited by Johnny Jazeix"],
                            colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["German", "Deutsch"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label, "Oliver van der Bürie",
                            colors[top % 2], "", 6)

        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Hebrew", "תירבע"], colors[top % 2], "", 6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label, ["Ori Hoch"],
                            colors[top % 2], "", 6)

        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Italian", "Italiano"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label, "Giuliano", colors[top % 2],
                            "", 6)

        # column 2
        top = 1
        left = middle
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Polish", "Polski"], colors[top % 2], "", 6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            ["Kamila Roszak-Imiolek", "Ireneusz Imiolek"], colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Portuguese", "Português"], colors[top % 2],
                            "", 6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label, "Américo Monteiro",
                            colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Russian", "Русский"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            ["Anton Kayukov (Антон Каюков)", "Alexey Loginov (Алексей Логинов)"], colors[top % 2], "",
                            6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Serbian", "Српски"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            ["Miroslav Nikolic (Мирослав Николић)"], colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Spanish", "Español"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            ["Miriam Ruiz (http://www.miriamruiz.es)", "updated by: Mario Izquierdo"],
                            colors[top % 2], "", 6)
        top += 1
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Ukrainian", "Українська"], colors[top % 2],
                            "", 6)
        self.board.add_unit(left + lang_width, top, credits_width, 1, classes.board.Label,
                            "Yuri Chornoivan (Юрій Чорноіван)", colors[top % 2], "",
                            6)

        # due to the number of people working on this one - it stays at the bottom and spreads across 2 columns
        # update top - to the height of the tallest column
        top = 8
        left = 0
        self.board.add_unit(left, top, lang_width, 1, classes.board.Label, ["Greek", "Ελληνικά"], colors[top % 2], "",
                            6)
        self.board.add_unit(left + lang_width, top, data[0] - lang_width, 1, classes.board.Label, [
            "Στέλιος, versys650gr, sdim, lucinos and other members of The Official Greek Community of Linux Mint,",
            "updated and edited by Alexandros Moskofidis (Αλέξανδρος Μοσκοφίδης)"], colors[top % 2], "", 6)

        top += 1
        self.board.add_unit(0, top, data[0], 1, classes.board.Letter, "<<", colors[top % 2], "", 0)
        self.btn_back = self.board.ships[-1]


        # self.outline_all(1,1)
        for each in self.board.units:
            each.font_color = font_color
            each.align = 1
        self.board.units[0].align = 0

        self.btn_back.font_color = (255, 0, 0)
        self.btn_back.highlight = False
        self.btn_back.readable = False

    def handle(self, event):
        gd.BoardGame.handle(self, event)  # send event handling up
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                active = self.board.active_ship
                if active >= 0:
                    if self.board.ships[active] == self.btn_back:
                        self.mainloop.m.start_hidden_game(0)

    def update(self, game):
        game.fill((255, 255, 255))
        gd.BoardGame.update(self, game)  # rest of painting done by parent

    def check_result(self):
        pass
