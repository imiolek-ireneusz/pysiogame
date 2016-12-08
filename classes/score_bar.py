# -*- coding: utf-8 -*-

import os
import pygame
import sys


class PScoreItem(pygame.sprite.Sprite):
    def __init__(self, score_bar, pos_rect):
        pygame.sprite.Sprite.__init__(self)
        self.score_bar = score_bar
        self.pos_rect = pos_rect
        self.image = pygame.Surface([pos_rect[2], pos_rect[3]])
        self.rect = self.image.get_rect()
        self.rect.topleft = [pos_rect[0], pos_rect[1]]
        self.bg_color = self.score_bar.fbg_color
        self.update_me = True

    def update(self):
        self.image.fill(self.bg_color)

    def handle(self, event):
        pass

    def onClick():
        pass


class PToggleBtn(PScoreItem):
    def __init__(self, score_bar, pos_rect, img_on, img_off, fsubmit, fargs):
        PScoreItem.__init__(self, score_bar, pos_rect)
        self.enabled = True
        self.img_loaded = False
        self.fsubmit = fsubmit
        self.fargs = fargs
        # try:
        if True:
            self.img_on = pygame.image.load(os.path.join('res', 'images', img_on)).convert()
            self.img_off = pygame.image.load(os.path.join('res', 'images', img_off)).convert()
            self.img_pos = (0, 0)
            self.img_loaded = True
        # except IOError:
        else:
            pass

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            if self.enabled:
                self.enabled = False
                self.fsubmit(False)
            else:
                self.enabled = True
                self.fsubmit(True)
            self.score_bar.update_me = True
            self.update()

    def update(self):
        PScoreItem.update(self)
        if self.img_loaded:
            if self.enabled:
                self.image.blit(self.img_on, self.img_pos)
            else:
                self.image.blit(self.img_off, self.img_pos)


class PSelectBtn(PScoreItem):
    def __init__(self, score_bar, pos_rect, img_src1, img_src2, fsubmit, fargs):
        PScoreItem.__init__(self, score_bar, pos_rect)
        self.enabled = True
        self.img_loaded = False
        self.fsubmit = fsubmit
        self.fargs = fargs
        try:
            self.img1 = pygame.image.load(os.path.join('res', 'images', img_src1)).convert()
            self.img2 = pygame.image.load(os.path.join('res', 'images', img_src2)).convert()
            self.img_pos = (0, 0)
            self.img_loaded = True
        except IOError:
            pass

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.fsubmit(self.fargs)
            self.score_bar.update_me = True

    def update(self):
        PScoreItem.update(self)
        if self.img_loaded:
            if self.score_bar.mainloop.scheme_code == self.fargs:
                self.image.blit(self.img2, self.img_pos)
            else:
                self.image.blit(self.img1, self.img_pos)


class PLabel(PScoreItem):
    def __init__(self, score_bar, pos_rect, value):
        PScoreItem.__init__(self, score_bar, pos_rect)
        self.font_color = (255, 255, 255)
        self.value = value
        self.bold = False

    def update(self):
        PScoreItem.update(self)
        if self.update_me:
            if sys.version_info < (3, 0):
                try:
                    val = unicode(self.value, "utf-8")
                except UnicodeDecodeError:
                    val = self.value
                except TypeError:
                    val = self.value
            else:
                val = self.value
            if self.bold is None:
                fnt = self.score_bar.font_clock
            elif self.bold == True:
                fnt = self.score_bar.font_bold
            else:
                fnt = self.score_bar.font
            text = fnt.render("%s" % (val), 1, self.font_color)

            font_x = 0
            font_y = 3  # (self.pos_rect[3] - self.score_bar.font.size(val)[1])//2
            self.image.blit(text, (font_x, font_y))


class PLinkLabel(PLabel):
    def __init__(self, score_bar, pos_rect, value, fsubmit):
        PLabel.__init__(self, score_bar, pos_rect, value)
        self.font_color = (255, 104, 104)
        self.font_hover = (255, 55, 55)
        self.font_normal = (255, 104, 104)
        self.fsubmit = fsubmit

    def handle(self, event):
        if event.type == pygame.MOUSEBUTTONUP:
            self.onClick()

    def onClick(self):
        self.fsubmit()


class ScoreBar:
    def __init__(self, mainloop):
        # self.bg_color = (45,45,45)
        self.mainloop = mainloop
        self.lang = self.mainloop.lang
        self.bg_color = (70, 70, 70)
        self.fbg_color = (45, 45, 45)
        self.update_me = True
        self.widget_list = None
        self.mouse_over = False

        self.points = int(round((50 * 72 / 96) / 4, 0))
        self.font = pygame.font.Font(
            os.path.join('res', 'fonts', self.mainloop.config.font_dir, self.mainloop.config.font_name_2),
            (int(self.points * 2.0)))
        self.font_bold = pygame.font.Font(
            os.path.join('res', 'fonts', self.mainloop.config.font_dir, self.mainloop.config.font_name_1),
            (int(self.points * 2.0)))
        self.font_clock = pygame.font.Font(os.path.join('res', 'fonts', 'pysiogameFonts', 'pysiogameClock.ttf'),
                                           (int(self.points * 4.0)))
        """
        self.widget_list = pygame.sprite.LayeredUpdates()
        self.elements = []
        self.add_scroll_bar_elements()
        """

    def add_scroll_bar_elements(self):
        # toggle sounds
        l = 2
        self.elements.append(
            PToggleBtn(self, (l, 2, 28, 28), "score_sound_on.png", "score_sound_off.png", self.toggle_sound, None))
        l += 28 + 5
        # toggle espeak
        if self.mainloop.speaker.enabled:  # and self.mainloop.lang.voice is not None:
            self.elements.append(
                PToggleBtn(self, (l, 2, 28, 28), "score_espeak_on.png", "score_espeak_off.png", self.toggle_espeak,
                           None))
            l += 28 + 15
        else:
            l += 10
        l += 0
        self.elements.append(
            PSelectBtn(self, (l, 2, 28, 28), "score_hc_none.png", "score_hc_anone.png", self.switch_scheme, None))
        l += 28
        self.elements.append(
            PSelectBtn(self, (l, 2, 28, 28), "score_hc_wb.png", "score_hc_awb.png", self.switch_scheme, "WB"))
        l += 28
        self.elements.append(
            PSelectBtn(self, (l, 2, 28, 28), "score_hc_bw.png", "score_hc_abw.png", self.switch_scheme, "BW"))
        l += 28
        self.elements.append(
            PSelectBtn(self, (l, 2, 28, 28), "score_hc_by.png", "score_hc_aby.png", self.switch_scheme, "BY"))
        l += 28
        l += 10
        # score label
        # label = "Score" #self.lang.d["Score: "] + "0" #"Score: 12345"
        # w = self.font_bold.size(label)[0]
        self.elements.append(PLabel(self, (l, 2, 300, 28), ""))
        self.score = self.elements[-1]
        self.score.font_color = (136, 201, 255)
        self.score.bold = None
        # self.set_score(self.mainloop.)
        self.mainloop.game_board.update_score(0)
        # self.score.bold = True

        # logout link

        label = self.lang.d["(Log out)"][:]

        if sys.version_info < (3, 0):
            try:
                w0 = self.font.size(unicode(label, "utf-8"))[0]
            except:
                w0 = self.font.size(label)[0]
        else:
            w0 = self.font.size(label)[0]
        self.elements.append(PLinkLabel(self, (self.width - w0 - 5, 0, w0, 32), label, self.flogout))

        # name label
        label = self.mainloop.user_name

        # logged in as: label
        label2 = self.lang.d["Logged in as: "]

        w1 = self.font.size(label)[0]
        if sys.version_info < (3, 0):
            try:
                w2 = self.font.size(unicode(label2, "utf-8"))[0]
            except:
                w2 = self.font.size(label2)[0]
        else:
            w2 = self.font.size(label2)[0]
        if self.lang.ltr_text:
            l1 = self.width - w0 - w1 - 20
            l2 = self.width - w0 - w1 - w2 - 20
        else:
            l1 = self.width - w0 - w1 - w2 - 30
            l2 = self.width - w0 - w2 - 20
        self.elements.append(PLabel(self, (l1, 0, w1, 32), label))
        self.elements[-1].font_color = (136, 201, 255)

        self.elements.append(PLabel(self, (l2, 0, w2, 32), label2))

        for each in self.elements:
            self.widget_list.add(each)

        self.update()

    def set_score(self, new_score):
        # self.score.value = self.lang.d["Score: "] + str(new_score)
        # self.score.value = str(new_score)
        self.score.value = ""  # str(new_score)
        self.score.update_me = True
        self.update_me = True

    def resize(self):
        self.width = self.mainloop.game_board.layout.score_bar_pos[2]
        self.height = self.mainloop.game_board.layout.score_bar_pos[3]
        if self.widget_list is not None:
            self.widget_list.empty()
        self.widget_list = pygame.sprite.LayeredUpdates()
        self.elements = []
        self.add_scroll_bar_elements()
        self.update_me = True

    def update(self):
        # get toggle buttons states
        self.elements[0].enabled = bool(self.mainloop.config.settings["sounds"])
        self.elements[1].enabled = bool(self.mainloop.config.settings["espeak"])

    def draw(self, screen):
        # draw info bar
        self.update()
        score_bar_pos = self.mainloop.game_board.layout.score_bar_pos[:]
        rect = [0, 0, score_bar_pos[2], score_bar_pos[3] - 4]
        screen.fill(self.bg_color)
        pygame.draw.rect(screen, self.fbg_color, rect, 0)
        pygame.draw.line(screen, (255, 255, 255), [0, rect[3]], [rect[2], rect[3]], 1)

        for each in self.widget_list:
            each.update()

        self.widget_list.draw(screen)
        self.update_me = False

    def handle(self, event):
        if event.type == pygame.MOUSEMOTION or event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            self.on_mouse_over()
            pos = [event.pos[0] - self.mainloop.game_board.layout.score_bar_pos[0], event.pos[1]]
            for each in self.elements:
                if each.rect.topleft[0] + each.rect.width >= pos[0] >= each.rect.topleft[0] and each.rect.topleft[
                    1] + each.rect.height >= pos[1] >= each.rect.topleft[1]:
                    each.handle(event)
        else:
            pass

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

        self.mouse_over = True
        # print("enter score")

    def on_mouse_out(self):
        if self.mouse_over:
            self.mouse_over = False

    def flogout(self):
        self.mainloop.dialog.show_dialog(1, self.lang.d["Do you want to log out of the game?"])

    def toggle_sound(self, enable):
        self.update_me = True
        if enable:
            self.mainloop.config.settings["sounds"] = True
        else:
            self.mainloop.config.settings["sounds"] = False
        self.mainloop.config.settings_changed = True

    def toggle_espeak(self, enable):
        self.update_me = True
        if enable:
            self.mainloop.config.settings["espeak"] = True
            self.mainloop.speaker.talkative = True
        else:
            self.mainloop.config.settings["espeak"] = False
            self.mainloop.speaker.talkative = False
        self.mainloop.config.settings_changed = True

    def switch_scheme(self, scheme):
        self.mainloop.switch_scheme(scheme)
