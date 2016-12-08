# -*- coding: utf-8 -*-

import os
import pygame

from game_boards import game000


class LogoImg(pygame.sprite.Sprite):
    'holds the logo in top left corner'

    def __init__(self, mainloop):
        # Call the parent's constructor
        pygame.sprite.Sprite.__init__(self)
        self.mainloop = mainloop
        self.state = 2
        self.mouse_over = False
        self.image = pygame.Surface([166, 146])
        self.image.fill((60, 60, 60))

        self.rect = self.image.get_rect()
        self.rect.topleft = [0, 0]
        # self.img = self.image
        self.img_pos = (0, 0)
        try:
            self.img1 = pygame.image.load(os.path.join('res', 'images', "logo_n.png")).convert_alpha()
            self.img2 = pygame.image.load(os.path.join('res', 'images', "logo_h.png")).convert_alpha()
            self.img3 = pygame.image.load(os.path.join('res', 'images', "logo_a.png")).convert_alpha()
        except:
            pass
        self.update()
        # self.image.set_colorkey((255,75,0))

    def handle(self, event):
        if event.type == pygame.MOUSEMOTION:
            self.on_mouse_over()

        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:

            # for each in self.games_current:
            #    each.state = 0
            # self.games_current[row].state = 2

            if self.mainloop.m.active_o is not None:
                self.mainloop.m.active_o.state = 0
                self.mainloop.m.active_o = None
            if self.mainloop.m.active_cat_o is not None:
                self.mainloop.m.active_cat_o.deactivate()
                self.mainloop.m.active_cat_o = None
            if self.state < 2:
                self.mainloop.sfx.play(4)

            self.state = 2

            self.mainloop.m.active_cat = 0
            # self.tab_l_scroll = (self.scroll_l // self.scroll_step)

            self.mainloop.m.game_constructor = game000.Board  # self.games_current[row].game_constructor
            self.mainloop.m.game_variant = 0  # self.games_current[row].variant
            self.mainloop.m.active_game_id = 0
            self.mainloop.m.game_started_id = -1
            self.mainloop.m.tab_game_id = -5
            self.mainloop.m.tab_r_scroll = 0
            self.mainloop.redraw_needed = [True, True, True]

    def on_mouse_over(self):
        if not self.mouse_over:
            self.on_mouse_enter()

    def on_mouse_enter(self):
        if self.mainloop.mouse_over[0] is not None:
            self.mainloop.mouse_over[0].on_mouse_out()
        self.mainloop.mouse_over[0] = self
        if self.mainloop.mouse_over[1] is not None:
            self.mainloop.mouse_over[1].on_mouse_out()
        self.mainloop.mouse_over[1] = None
        if self.mainloop.mouse_over[2] is not None:
            self.mainloop.mouse_over[2].on_mouse_out()
        self.mainloop.mouse_over[2] = None

        if self.state != 2:
            self.state = 1

        self.mouse_over = True
        self.update()
        # print("enter (in logoimg.py)")
        self.mainloop.redraw_needed[2] = True

    def on_mouse_out(self):
        if self.mouse_over:
            self.mouse_over = False
            if self.state != 2:
                self.state = 0
            self.update()
            # print("out logoimg.py")
            self.mainloop.redraw_needed[2] = True

    def update(self):
        img = eval("self.img%i" % (self.state + 1))
        self.image.blit(img, self.img_pos)
