# -*- coding: utf-8 -*-

import classes.level_controller as lc
import classes.game_driver as gd
import pygame

import classes.board


class Board(gd.BoardGame):
    def __init__(self, mainloop, speaker, config,  screen_w, screen_h):
        self.level = lc.Level(self,mainloop,1,1)
        gd.BoardGame.__init__(self,mainloop,speaker,config,screen_w,screen_h,11,10)

    def create_game_objects(self, level = 1):
        self.board.draw_grid = False
        self.show_info_btn = False

        color1 = (220,220,220)
        color2 = (255,255,255)

        font_color = (40,40,40)
        data = [16,14]
        #stretch width to fit the screen size
        x_count = self.get_x_count(data[1],even=None)
        if x_count > 15:
            data[0] = x_count

        self.data = data

        self.vis_buttons = [0,0,0,0,1,0,1,0,0]
        self.mainloop.info.hide_buttonsa(self.vis_buttons)

        self.layout.update_layout(data[0],data[1])
        scale = self.layout.scale
        self.board.level_start(data[0],data[1],scale)

        self.board.board_bg.line_color = (200, 200, 200)
        if self.mainloop.scheme is not None:
            self.board.board_bg.line_color = self.mainloop.scheme.u_line_color
        self.board.board_bg.update_me = True

        self.board.add_unit(0,0,data[0],1,classes.board.Label,self.lang.d["Translators"],color2,"",4)
        top = 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["English & Polish","English & Polski"],color1,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Kamila Roszak-Imiolek, Ireneusz Imiolek"],color1,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Catalan","Català"],color2,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Guillem Jover","http://www.hadrons.org/~guillem/"],color2,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Finnish","Suomalainen"],color1,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Aapo Rantalainen"],color1,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["French","Français"],color2,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Gino Ingras", "edited by Johnny Jazeix"],color2,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["German","Deutsch"],color1,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,"Oliver van der Bürie",color1,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Greek","Ελληνικά"],color2,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Στέλιος, versys650gr, sdim, lucinos and other members of The Official Greek Community of Linux Mint,", "updated and edited by Alexandros Moskofidis (Αλέξανδρος Μοσκοφίδης)"],color2,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Hebrew","תירבע"],color1,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Ori Hoch"],color1,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Italian","Italiano"],color2,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,"Giuliano",color2,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Portuguese","Português"],color1,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,"Américo Monteiro",color1,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Russian","Русский"],color2,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Anton Kayukov (Антон Каюков)", "Alexey Loginov (Алексей Логинов)"],color2,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Spanish","Español"],color1,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,["Miriam Ruiz","http://www.miriamruiz.es"],color1,"",6)
        top += 1
        self.board.add_unit(0,top,3,1,classes.board.Label,["Ukrainian","Українська"],color2,"",6)
        self.board.add_unit(3,top,data[0]-3,1,classes.board.Label,"Yuri Chornoivan (Юрій Чорноіван)",color2,"",6)
        top += 1
        self.board.add_unit(0,top,data[0],1,classes.board.Letter,"<<",color1,"",0)
        self.btn_back = self.board.ships[-1]
        """
        self.board.add_unit(0,5,3,1,classes.board.Label,"French",color1,"",6)
        self.board.add_unit(3,5,data[0]-3,1,classes.board.Label,"Not Translated",color1,"",6)


        self.board.add_unit(0,9,3,1,classes.board.Label,"Finnish",color1,"",6)
        self.board.add_unit(3,9,data[0]-3,1,classes.board.Label,"Not Translated",color1,"",6)
        """

        #self.outline_all(1,1)
        for each in self.board.units:
            each.font_color = font_color
            each.align = 1
        self.board.units[0].align = 0

        self.btn_back.font_color = (255,0,0)
        self.btn_back.highlight = False
        self.btn_back.readable = False

    def handle(self,event):
        gd.BoardGame.handle(self, event) #send event handling up
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                active = self.board.active_ship
                if active >= 0:
                    if self.board.ships[active] == self.btn_back:
                        self.mainloop.m.start_hidden_game(0)

    def update(self,game):
        game.fill((255,255,255))
        gd.BoardGame.update(self, game) #rest of painting done by parent

    def check_result(self):
        pass
