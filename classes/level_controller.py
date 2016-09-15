# -*- coding: utf-8 -*-
import gc
import random
import time

#file initialising level control
class Level:
    def __init__(self,board,mainloop,gpl,lvl_count):
        self.game_board = board
        self.mainloop = mainloop
        self.next_pressed = False
        self.name = self.mainloop.user_name
        self.prev_lvl = -1 #used to check if level changed
        self.games_per_lvl = gpl #number of games to play in order to level up
        self.lvl_count = lvl_count #number of levels
        self.completed = 0 #how many times was this level completed - loaded from db later on
        self.completed_time = time.time()
        self.restart()

        self.dp = self.mainloop.lang.dp

    def restart(self):
        self.lvl = 1 #current level
        self.game_step = 1 #used to store number of games played in this level


    def levelup(self):
        self.mainloop.dialog.show_dialog(2,self.mainloop.lang.d["Ready to go to the next level?"],self.manual_levelup,self.reset_level)

    def manual_levelup(self,args=None):
        if self.lvl < self.lvl_count:
            self.lvl += 1
            self.mainloop.sfx.play(7)
            self.load_level_plus()

    def manual_leveldown(self):
        if self.lvl > 1:
            self.lvl -= 1
            self.mainloop.sfx.play(9)
            self.load_level_plus()

    def chapter_up(self):
        chs = self.game_board.chapters
        lch = len(chs)
        if lch > 1:
            current_chapter = self.get_current_chapter(chs,lch)
            if current_chapter < lch-1:
                self.lvl = chs[current_chapter+1]
                self.mainloop.sfx.play(7)
                self.load_level_plus()

    def chapter_down(self):
        chs = self.game_board.chapters
        lch = len(chs)
        if lch > 1:
            current_chapter = self.get_current_chapter(chs,lch)
            if self.lvl > chs[current_chapter] > 0:
                self.lvl = chs[current_chapter]
                self.mainloop.sfx.play(9)
                self.load_level_plus()
            elif chs[current_chapter] == self.lvl > 1:
                self.lvl = chs[current_chapter-1]
                self.mainloop.sfx.play(9)
                self.load_level_plus()

    def get_current_chapter(self,chs,lch):
        if self.lvl == self.lvl_count:
            return lch-1
        elif self.lvl == 1:
            return 0
        else:
            for i in range(0,lch-1):
                if chs[i] <= self.lvl < chs[i+1]:
                    return i
            return None

    def update_level_dict(self):
        #saved_levels = self.game_board.mainloop.m.saved_levels
        active_item = self.game_board.mainloop.m.games[self.game_board.mainloop.m.active_game_id]
        #saved_levels[active_item.game_constructor][str(active_item.variant)] = self.lvl

        #print(self.lvl)
        #print("self.lvl: %d" % self.lvl)
        #self.game_board.mainloop.m.saved_levels[active_item.dbgameid] = self.lvl

        self.game_board.mainloop.db.update_cursor(self.game_board.mainloop.userid, self.game_board.active_game.dbgameid, self.lvl)
        self.game_board.mainloop.m.load_levels()


    def welcome(self):
        pass

    def game_over(self,tts=""):
        #self.load_level()
        if tts=="":
            self.game_board.say(self.dp["Game Over!"],6)
        else:
            self.game_board.say(tts,6)
        self.dialog_type = 1
        self.game_step -= 1
        self.game_board.show_msg = True
        self.game_board.mainloop.redraw_needed[0] = True


    def game_won(self,tts=""):
        #print("Congratulations you won the game")
        if tts != None:
            self.game_board.say(self.dp["Congratulations! Game Completed."],6)
        self.restart()
        self.game_step = 1
        self.load_level()
        self.dialog_type = 0
        self.game_board.show_msg = True
        self.game_board.mainloop.score = 0


    def try_again(self, silent = False):
        self.mainloop.info.btns[0].img = self.mainloop.info.btns[0].img_3
        self.game_board.changed_since_check = False
        if not silent:
            self.mainloop.sfx.play(8)
        #self.game_board.say("Not really",6)

    def next_board(self,tts=""):
        if not self.next_pressed:
            self.game_board.changed_since_check = False
            self.game_board.mainloop.redraw_needed[0] = True
            if self.game_step < self.games_per_lvl:
                if self.mainloop.speaker.talkative:
                    if tts=="":
                        #pick a praise phrase
                        index = random.randrange(0,len(self.dp["Great job!"]))
                        praise = self.dp["Great job!"][index]
                        self.game_board.say(praise,6)
                    elif tts != None:
                        self.game_board.say(tts,6)
                else:
                    self.mainloop.sfx.play(14)
                self.dialog_type = 0
                self.game_board.show_msg = True
                self.completed_time = time.time()
            else:
                self.game_board.mainloop.db.update_completion(self.game_board.mainloop.userid, self.game_board.active_game.dbgameid, self.lvl)
                if self.lvl < self.lvl_count:
                    self.levelup()
                    if tts != None:
                        self.game_board.say(self.dp["Perfect! Level completed!"],6)
                    #self.dialog_type = 0
                    #self.game_board.show_msg = True
                else:
                    self.game_won(tts)
                self.completed_time = time.time()
            self.next_pressed = True

    def next_board_load(self,tts=""):
        if self.game_step < self.games_per_lvl:
            self.game_step += 1
            self.load_level()
        else:
            if self.lvl < self.lvl_count:
                self.levelup()
            else:
                pass #self.game_won()

    def load_level(self):
        self.game_board.create_game_objects(self.lvl)

        gc.collect()
        if self.game_board.game_type == "Board":
            self.game_board.board.board_bg.update_me = True
        self.update_level_dictx()
        self.game_board.mainloop.redraw_needed = [True, True, True]
        self.next_pressed = False

    def reset_level(self):
        self.game_step = 1
        self.load_level()


    def update_level_dictx(self):
        self.update_level_dict()
        self.completed = self.game_board.mainloop.db.query_completion(self.game_board.mainloop.userid, self.game_board.active_game.dbgameid, self.lvl)

    def load_level_plus(self):
        self.game_step = 1
        self.load_level()

