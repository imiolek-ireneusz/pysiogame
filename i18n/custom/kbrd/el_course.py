# -*- coding: utf-8 -*-

from i18n.custom.word_lists.el_di import di
from classes.extras import get_word_list, word_typing_course
from i18n.custom.kbrd.en_cinderella import cinderella
base_qwerty = [
#λvλ1 - λearning home keys asdf jkλ
[[3,3,3,3,3,3],
["ασδφ φδσα ", "ξκλ λκξ ", "ασδφ ξκλ λκξ φδσα ", "αξσκδλφ φλδκσξα ", "αλσκδξφ φξδκσλα ", "αδξλσκφ λξδακφσ "]
],

#λωλ2 - αδδινγ γ ανδ η
[[3,3,3,3,3,3],
["ασδφγ γφδσα ", "ηξκλ λκξη ", "ασδφγ ηξκλ λκξη γφδσα ", "αξσκδλφηγ γηφλδκσξα ", "αλσκδξφηγ γηφξδκσλα ", "αδγηκλ σφηγξλ "]
],

#λωλ3 - τραινινγ λεφτ ηανδ - λεαρνινγ λεττερσ - ςερτ
[[4, 4, 5,3,3,3,3,3,3,3,3],
["φρφ φτφ ", "αα σςσ δεδ φρφ φτφ ", "αςσεδρφτγ γτφρδεσςα ", "αεδτγςσρφ φρσςγτδεα ", "ασςεσδ ερδφρτφγ ", "γφτρφδρε δσεςσα ", "αςδργ τφεσ ", "σεφτ γρδςα ", "αρφ φρα ", "αεφς ςφεα ", "εαρσςδεφ φεδςσραε "]
],

#λωλ4 - αδδινγ ριγητ ηανδ - λεαρνινγ λεττερσ - νμ
[[4,4,4,3,3,3,3],
["ηναξμσ κνδλμφ ", "ναν μσμς ", "νςμενρμ ", "ξςκελρ ρλεκςξ ", "τξφρκφεκδ ςλσλα ", "αξςσκεδλ ρφκτφξ ", "ναμσξδ κφλγφ "]
],

#λωλ5 - λεαρνινγ λεττερσ - υθιοπ
[[4,4,4, 3,3,3,3],
["ξυξ ξθξ ", "ξυξ ξθξ κικ λολ ποπ ", "ξνυξ ξμθξ ", "κιθξκ λοικξ ", "πολκιθξ ξνηθξ κμξικ ", "πλοκιξθηυ ηυξθκιλοπ ", "υηικθξολπ ποκθη "]
],

#λωλ6 - λεαρνινγ λεττερσ - ζχψωβ
[[4,4,4, 3,3],
["φβφ φωφ ", "φβφ φωφ δψδ σχσ αζα ", "αςδχ σεφψ δργω ", "αζσ σχδ δψφ φωγ ", "αζσχδψφωβ βωφψδχσζα "]
],

#λωλ7 - λεαρνινγ θππερψασε λεττερσ
[[3,3,3],
["ασ σδ δφ φγ γη ηξ ξκ κλ ", "α ςσ εδ ρφ τφ υξ θξ ικ ολπ ", "ζα χσ ψδ ωφ βφ νξ μξ "]
],

#λωλ9 - θιψκ ηομε κευσ ρεωισιον
[[2,2],
["ααζα σςσχσ δεδψδ φρφτφωφβφγφ ", "ξυξθξνξμξηξ κικλολπ "]
]]
"""
#λωλ8 - λεαρνινγ ποσιτιον οφ ", . ; : ?" !
[[2,2],
["κ,κ λ.λ ;π; ", "οκ? οκ! οκ, οκ. "]
],
"""
course = []

#add English qwerty course
course.extend(base_qwerty)

#add Language specific word list - words taken from en_gb_di.py file.
word_list = get_word_list(di)
word_course = word_typing_course(word_list)
course.extend(word_course)
#course.extend(cinderella)
