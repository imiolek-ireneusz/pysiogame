# -*- coding: utf-8 -*-

import gettext

#FAO Translators:
#First of all thank you for your interest in translating this game,
#I will be grateful if you could share it with the community -
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible).
#The colour names in other languages than English are already in smaller font.

#when translating the "d" dictionary please translate the values
#and leave keys as they are (the keys are sometimes shortened to save on space)

class I18n():
    def __init__(self):
        self.translate()


    def translate(self):

        #the following line is added to force the xgettext to add these entries
        #self.fruit = [gettext.ngettext("green apple","green apples",1), gettext.ngettext("red apple","red apples",1), gettext.ngettext("strawberry","strawberries",1), gettext.ngettext("pear","pears",1), gettext.ngettext("orange","oranges",1), gettext.ngettext("onion","onions",1), gettext.ngettext("tomato","tomatoes",1), gettext.ngettext("lemon","lemons",1), gettext.ngettext("cherry","cherries",1), gettext.ngettext("pepper","peppers",1), gettext.ngettext("carrot","carrots",1), gettext.ngettext("banana","bananas",1), gettext.ngettext("watermelon","watermelons",1)]

        self.shape_names = [_("Equilateral Triangle"), _("Isosceles Triangle"), _("Obtuse Triangle"), _("Right Triangle"), _("Acute Triangle"), _("Square"), _("Rectangle"), _("Right Trapezium"), _("Isosceles Trapezium"), _("Rhombus"), _("Parallelogram"), _("Pentagon"), _("Hexagon"), _("Circle"), _("Ellipse")]
        self.solid_names = [_("Cube"), _("Square Prism"), _("Triangular Prism"), _("Square Pyramid"), _("Triangular Pyramid"), _("Sphere"), _("Cylinder"), _("Cone"), _("Torus")]

        self.d = dict()
        self.dp = dict()
        self.b = dict()
        self.b["Default Language:"] = _("Default Language:")
        self.b["Guest"] = _("Guest")
        self.b["Hi Stranger"] = _("Hi Stranger :) Would you like to log in so we know who you are?")
        self.b["Log in:"] = _("Log in:")
        self.b["user name:"] = _("user name:")
        self.b["password:"] = _("password:")
        self.b["remember me"] = _("remember me")
        self.b["Login"] = _("Login")
        self.b["Add new user:"] = _("Add new user:")
        self.b["confirm password:"] = _("confirm password:")
        self.b["Register"] = _("Register new user")
        self.b["Administrator Login:"] = _("Administrator Login:")
        self.b["User Management"] = _("User Management")
        self.b["Please select"] = _("Please select a user from the list.")
        self.b["delete user"] = _("Delete user")
        self.b["Delete"] = _("Delete")
        self.b["Cancel"] = _("Cancel")
        self.b["user deleted"] = _("%s deleted from database.")
        self.b["Failed to delete"] = _("Failed to delete the user.")


        self.b["Preferences"] = _("Preferences")
        self.b["switch to full screen after login"] = _("switch to full screen after login")
        self.b["display languages with uncompleted translations"] = _("display languages with uncompleted translations")
        self.b["require password to log in"] = _("require password to log in")
        self.b["require password to access admin area"] = _("require password to access admin area")
        self.b["Update admin's password:"] = _("Update admin's password:")
        self.b["previous password:"] = _("previous password:")
        self.b["new password:"] = _("new password:")
        self.b["confirm new password:"] = _("confirm new password:")
        self.b["Create admin's account:"] = _("Create admin's account:")
        self.b["admin's user name:"] = _("admin's user name:")
        self.b["admin's password:"] = _("admin's password:")
        self.b["confirm admin's password:"] = _("confirm admin's password:")
        self.b["Save"] = _("Save")

        self.b["Please enter user name (at least 3 characters long)"] = _("Please enter user name (at least 3 characters long)")
        self.b["Please enter password (at least 4 characters long)"] = _("Please enter password (at least 4 characters long)")
        self.b["This username and password combination doesn't exist."] = _("This username and password combination doesn't exist.")
        self.b["This username doesn't exist."] = _("This username doesn't exist.")

        self.b["Passwords don't match"] = _("Passwords don't match")
        self.b["%s added"] = _("%s added")
        self.b["This user name already exists, please choose a different one"] = _("This user name already exists, please choose a different one")

        self.b["Admin's password has been updated"] = _("Admin's password has been updated")
        self.b["ERROR: This operation is not allowed at this point"] = _("ERROR: This operation is not allowed at this point")
        self.b["Please enter previous password (at least 4 characters long)"] = _("Please enter previous password (at least 4 characters long)")
        self.b["Please enter new password (at least 4 characters long)"] = _("Please enter new password (at least 4 characters long)")
        self.b["Previous password doesn't seem to be in the database"] = _("Previous password doesn't seem to be in the database")

        self.b["registered:"] = _("Registered:")
        self.b["last login:"] = _("Last login:")

        self.b["Prefs saved..."] = _("Preferences saved...")
        self.b["Score: "] = _("Score: ")

        self.b["Select age group:"] = _("Select age group:")
        self.b["preschool"] = _("preschool")
        self.b["Year 1"] = _("Year 1")
        self.b["Year 2"] = _("Year 2")
        self.b["Year 3"] = _("Year 3")
        self.b["Year 4"] = _("Year 4")
        self.b["Year 5"] = _("Year 5")
        self.b["Year 6"] = _("Year 6")

        self.b["all groups"] = _("show all")
        self.b["show activities for:"] = _("show activities for:")

        #self.d["Educational Activity Pack for Kids"] = _("Educational Activity Pack for Kids")
        self.d["Credits_long"] = _("Laby, 2010 by Mehdi Cherti (mehdidc) \n Sounds by various authors who contributed their works to freesound.org. \n Images by various authors who contributed their works to openclipart.org (Public Domain) and http://www.art4apps.org/ - Art4Apps by Smart4Kids - under a Creative Commons License (CC BY-SA). \n Please view credits.txt for more info about authors of media files used in this project")
        self.d["Lic_title"] = _("Licence")
        self.d["Lic_desc"] = _("This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. You should have received a copy of the GNU General Public License along with this program.  If not, see <http://www.gnu.org/licenses/>.")
        self.d["A little set of educational apps for kids"] = _("A little set of educational apps for kids")

        self.d["Logged in as: "] = _("Logged in as: ")
        self.d["(Log out)"] = _("(Log out)")
        self.d["Addition Table"] = _("Addition Table")

        #game start
        self.d["Hello"] = _("Hello")
        self.d["Welcome back."] = _("Welcome back in the game.")

        #settings
        #self.d["Preferences"] = _("Preferences")
        self.d["Language"] = _("Language")
        self.d["Translations"] = _("Translations")
        #self.d["Reader"] = _("eSpeak")
        #self.d["Read Instructions"] = _("Read Instructions at the start of games")

        #menu categories
        self.d["Info Category"] = _("Info & Settings")
        self.d["Keyboard & Mouse"] = _("Keyboard & Mouse")
        self.d["Discover Letters"] = _("Discover Letters")
        self.d["Learn Words"] = _("Learn New Words")
        self.d["Maths"] = _("Mathematics")
        self.d["Numbers & Basic Operations"] = _("Numbers & Basic Operations")
        self.d["Basic Operations - exercises"] = _("Basic Operations - Exercises")
        self.d["Sorting and Comparing"] = _("Sorting and Comparing")
        self.d["Geometry"] = _("Geometry and Shape Recognition")
        self.d["Art"] = _("Art and Colour")
        self.d["Memory"] = _("Memory")
        self.d["Games & Mazes"] = _("Games & Mazes")
        self.d["Multiplayer"] = _("Multiplayer Games")

        #games
        self.d["About."] = _("About.")
        self.d["Game info..."] = _("Game info...")
        self.d["Credits"] = _("Copyright & Credits")
        self.d["Hit the Mole"] = _("Hit the Mole")
        self.d["Letters"] = _("Letters")
        self.d["Letter Flashcards"] = _("Learn Letters with Flashcards")
        self.d["Learn to Write"] = _("Learn to Write")
        self.d["Trace Letters"] = _("Trace Letters and Numbers")
        self.d["Complete the ABC"] = _("Complete the ABC")
        self.d["English"] = _("English")
        self.d["in your language"] = _("Your language") #_("English 2") #in your Language
        self.d["Sorting Letters"] = _("Sorting Letters")
        self.d["Lowercase Letters"] = _("Lowercase Letters")
        self.d["Uppercase Letters"] = _("Uppercase Letters")
        self.d["Word Builder"] = _("Word Builder")
        self.d["Word Maze"] = _("Word Maze")
        self.d["Collect all"] = _("Collect all letters in the right order")
        self.d["Word Maze + 4"] = _("Word Maze + 4")
        self.d["Numbers"] = _("Numbers")
        self.d["Number Flashcards"] = _("Learn Numbers with Flashcards")
        self.d["Learn to Count"] = _("Learn to Count")
        self.d["Basic Addition"] = _("Basic Addition")
        self.d["Basic Subtraction"] = _("Basic Subtraction")
        self.d["Shopping List"] = _("Shopping List")
        self.d["Plus or Minus"] = _("Plus or Minus")
        self.d["Basic Operations"] = _("Basic Operations")
        self.d["Multiplication Table"] = _("Multiplication Table")
        self.d["Find the product"] = _("Find the product")
        self.d["Find the multiplier"] = _("Find the multiplier")
        self.d["Division"] = _("Division")
        self.d["Sorting Numbers"] = _("Sorting Numbers")
        self.d["Number Comparison"] = _("Number Comparison")
        self.d["Addition & Subtraction"] = _("Addition & Subtraction")
        self.d["Comparison"] = _("Comparison")
        self.d["Fractions"] = _("Fractions")
        self.d["Decimal Fractions"] = _("Decimal Fractions")
        self.d["Even or Odd"] = _("Even or Odd")
        self.d["Shapes"] = _("Shapes")
        self.d["Shape Flashcards"] = _("Learn Shapes with Flashcards")
        self.d["Solids"] = _("Solids")
        self.d["Solid Flashcards"] = _("Solid Geometry with Flashcards")
        self.d["Shape Matching"] = _("Shape Matching")
        self.d["help me find my shadow"] = _("help me find my shadow")
        self.d["Paint"] = _("Paint")
        self.d["Colour Matching"] = _("Colour Matching")
        self.d["label the colours"] = _("label the colours")
        self.d["Follow the Arrows"] = _("Follow the Arrows")
        self.d["remember the directions"] = _("remember the directions")
        self.d["Photographic Memory"] = _("Photographic Memory")
        self.d["Training"] = _("Training")
        self.d["Photographic Memory"] = _("Photographic Memory")
        self.d["Automatic Levels"] = _("Automatic Levels")
        self.d["Mouse Maze"] = _("Mouse Maze")
        self.d["Let's have some cheese"] = _("Let's have some cheese")
        self.d["Sheep Maze"] = _("Sheep Maze")
        self.d["Find the rest"] = _("Find the rest of the herd")
        self.d["Connect"] = _("Connect")
        self.d["Balloons with threads"] = _("Balloons with threads")
        self.d["Fifteen"] = _("Fifteen")
        self.d["With a Twist"] = _("With a Twist")

        #game instructions
        self.d["Drag the slider"] = _("Drag the slider up or down so that the right sign is in the red square.")
        self.d["Take your sheep"] = _("Take your sheep to the rest of the herd.")
        self.d["Check the shopping list"] = _("Check the shopping list and drag all needed items into the basket.")
        self.d["Drag lt"] = _("Drag one of the <, > or = (lesser, greater or equal) to the red square.")
        self.d["Drag lt2"] = _("Drag one of the lesser, greater or equal to the red square.")
        self.d["Re-arrange right"] = _("Re-arrange the above numbers so they are in the right order")
        self.d["Complete abc"] = _("Complete the abc using the letters above.")
        self.d["Write a word:"] = _("Write a word:")
        self.d["Find and separate"] = _("Find and separate the Even Numbers from the Odd Numbers in the above series.")
        self.d["Re-arrange alphabetical"] = _("Re-arrange the above letters so they are in the alphabetical order.")
        self.d["Re-arrange ascending"] = _("Re-arrange the above numbers so they are in the ascending order.")

        #game dialogs
        self.d["Please try again."] = _("Please try again.")
        self.d["Sorry! It is wrong."] = _("Sorry! It is wrong.")
        self.d["Perfect! Task solved!"] = _("Perfect! Task solved!")
        self.d["work harder"] = _("You need to work a little bit harder next time.")

        #level_controller
        self.d["Game Over!"] = _("Game Over!")
        self.d["Congratulations! Game Completed."] = _("Congratulations! You have completed all tasks in this game.")
        self.d["Great job!"] = [_("Great job!"),_("Perfect!!!"),_("Awesome!"),_("Fantastic job!"),_("Well done!")]
        self.d["Perfect! Level completed!"] = _("Perfect! Level completed!")

        #game specific labels:
        self.d["area:"] = _("area:")
        self.d["perimeter:"] = _("perimeter:")
        self.d["circumference:"] = _("circumference:")
        self.d["surface area:"] = _("surface area:")
        self.d["volume:"] = _("volume:")
        self.d["Perfect!"] = _("Perfect!")
        self.d["divided by"] = _("divided by")
        self.d["multiplied by"] = _("times")
        self.d["equals"] = _("equals")
        self.d["Shopping List"] = _("Shopping List")
        self.d["Even"] = _("Even")
        self.d["Odd"] = _("Odd")
        self.d["white"] = _("white")
        self.d["black"] = _("black")
        self.d["grey"] = _("grey")
        self.d["red"] = _("red")
        self.d["orange"] = _("orange [color]")
        self.d["yellow"] = _("yellow")
        self.d["olive"] = _("olive")
        self.d["green"] = _("green")
        self.d["sea green"] = _("sea green")
        self.d["teal"] = _("teal")
        self.d["blue"] = _("blue")
        self.d["navy"] = _("navy")
        self.d["purple"] = _("purple")
        self.d["violet"] = _("violet")
        self.d["magenta"] = _("magenta")
        self.d["indigo"] = _("indigo")
        self.d["pink"] = _("pink")
        self.d["maroon"] = _("maroon")
        self.d["brown"] = _("brown")
        self.d["aqua"] = _("aqua")
        self.d["lime"] = _("lime")

        #new
        self.d["Keyboard Skills"] = _("Rainbow Keyboard")
        self.d["Touch Typing"] = _("Touch Typing Tutor")
        self.d["Translators"] = _("Translators")
        self.d["English Alphabet"] = _("English Alphabet")
        self.d["Your Alphabet"] = _("Your Alphabet")

        #new in 0.3.0
        self.d["Paint Mixer"] = _("Mixing Colours for Painting")
        self.d["Mixing RYB"] = _("Mix red, yellow, blue, black and white paint")

        self.d["Light Mixer"] = _("Additive Colour Mixing - Light")
        self.d["Mixing RGB"] = _("Mix red, green and blue light to get other colours")

        self.d["Ink Mixer"] = _("Subtractive Colour Mixing - Paints, Dyes, Inks")
        self.d["Mixing CMY"] = _("Mix cyan, magenta and yellow paint to get other colours")

        self.d["Find the colour of the circle"] = _("Find the colour of the circle")
        self.d["Adjust CMY"] = _("Adjust the amount of cyan, magenta and yellow paint")
        self.d["Adjust RGB"] = _("Adjust the intensity of red, green and blue light")

        #the following is used by colour matching games in spoken hints
        #ie. "more red, less green, blue is ok")
        #self.d["more color"] = "more"
        #self.d["less color"] = "less"
        #self.d["color is ok"] = "is ok"

        #new in 0.3.1
        self.d["brush size"] = _("brush size")

        #new in 0.3.2
        self.d["TicTacToe2"] = _("Noughts and Crosses 2")
        self.d["TicTacToe3"] = _("Noughts and Crosses 3")

        self.d["multiline-tictactoe"] = _("Get as many lines of 3 as possible to win")


        self.d["Player"] = _("Player")
        self.d["Won"] = _("Won")
        self.d["Game Draw"] = _("Draw")
        self.d["UserName"] = _("User Name")
        self.d["Match Animals Memory"] = _("Match Animals - Memory Game")
        self.d["Match Fruits"] = _("Match Fruits - Memory Game")
        self.d["Match Vegetables"] = _("Match Vegetables - Memory Game")
        self.d["Match Numbers"] = _("Match Numbers - Memory Game")
        self.d["Find pairs"] = _("Find matching pairs of the same image")

        self.d["Sliced Images"] = _("Image Slider")
        self.d["Sliced Animals"] = _("Animal Slider")
        self.d["Sliced Fruits"] = _("Fruit Slider")
        self.d["Sliced Numbers"] = _("Number Slider")

        self.d["Fraction Groups"] = _("Fraction Groups")
        self.d["Percentages"] = _("Percentages")
        self.d["Ratios"] = _("Ratios")
        self.d["Fract instr0"] = _("Match fraction charts on the right to the ones on the left")
        self.d["Fract instr1"] = _("Match fraction charts and fractions on the right to the fraction charts on the left")
        self.d["Fract instr2"] = _("Match fraction charts to the fractions on the left")
        self.d["Fract instr3"] = _("Match fraction charts, fractions and decimal fractions on the right to their percentage representations")
        self.d["Fract instr4"] = _("Match charts to the ratios on the left. Ratios are expressed as ratio of coloured pieces to white pieces")

        self.d["Maths Matching Game"] = _("Maths Matching Game")
        self.d["Addition"] = _("Addition")
        self.d["Subtraction"] = _("Subtraction")
        self.d["Multiplication"] = _("Multiplication")
        self.d["Division"] = _("Division")

        self.d["Check for newer version..."] = _("Check for newer version, report bugs, discuss, translate or review this project at:")
        self.d["Match numbers to their spelling"] = _("Match numbers to their spelling")
        self.d["Number Spelling"] = _("Number Spelling")
        self.d["Match Animals"] = _("Match Animals")
        self.d["Find all matching animals"] = _("Find all matching animals")
        self.d["Match animals to their shadows"] = _("Match animals to their shadows")

        self.d["ShapeMaker"] = _("Shape Maker")

        self.d["draw_instr1"] = _("Shape to draw: %s")
        self.d["draw_instr2"] = _("Shape to draw: %s") #if the following size_instr turn out to be too long the beginning can be moved here, ie. d["draw_instr2"] = _("Shape to draw: %s, such that"
        self.d["size_instr_0"] = _("such that lengths of its bases are equal to %d and %d and height to %d") #for trapeziums
        self.d["size_instr_1"] = _("such that lengths of its sides are equal to %d") #square
        self.d["size_instr_2"] = _("such that lengths of its sides are equal to %d and %d") #rectangle
        self.d["size_instr_3"] = _("such that lengths of its 2 parallel bases are equal to %d and height to %d") #for parallelogram
        self.d["size_instr_4"] = _("such that length of its base is equal to %d and height to %d") #for triangles incl. isosceles triangles
        self.d["size_instr_5"] = _("such that lengths of its catheti are equal to %d and %d") #for right triangles
        self.d["size_instr_6"] = _("such that lengths of both of its catheti are equal to %d") #for right isosceles triangles
        self.d["size_instr_7"] = _("such that length of its hypotenuse is equal to %d") #for right isosceles triangles
        self.d["size_instr_8"] = _("such that length of one of its sides is equal to %d and height to %d") #for obtuse triangles
        self.d["size_instr_9"] = _("such that length of its radius is equal to %d") #for circles

        """
        self.d["hypotenuse"] = "hypotenuse" #przeciwprostokątna
        self.d["cathetus"] = "cathetus" #przyprostokątna #leg / periphrasis
        self.d["catheti"] = "catheti" #przyprostokątne #plular
        """

        self.d["square"] = _("Square")
        self.d["rectangle"] = _("Rectangle")
        self.d["right_trapezium"] = _("Right Trapezium")
        self.d["iso_trapezium"] = _("Isosceles Trapezium")
        self.d["rhombus"] = _("Rhombus")
        self.d["parallelogram"] = _("Parallelogram")
        self.d["quadrilateral"] = _("Quadrilateral")
        self.d["trapezium"] = _("Trapezium")
        self.d["u_trapezium"] = _("Trapezium ")
        self.d["triangle"] = _("Triangle")
        self.d["squished_quadi"] = _("Ouch... squished quadrilateral") #used to label a drawn "quadrilateral" with angles: 0º, 180º, 0º, 180º - all points on one line

        self.d["equi_tria"] = _("Equilateral Triangle")
        self.d["iso_tria"] = _("Isosceles Triangle")
        self.d["obtuse_tria"] = _("Obtuse Triangle")
        self.d["right_tria"] = _("Right Triangle")
        self.d["acute_tria"] = _("Acute Triangle")
        self.d["right_iso_tria"] = _("Right isosceles triangle")
        self.d["obtuse_iso_tria"] = _("Obtuse isosceles triangle")
        self.d["acute_iso_tria"] = _("Acute isosceles triangle")
        self.d["squished_tria"] = _("Ouch... squished triangle") #used to label a drawn "triangle" with angles: 0º, 180º, 0º - all points on one line
        self.d["circle"] = _("Circle")
        self.d["triangle_not_really"] = _("Triangle? Well, not really...") #used to label a drawn "quadrilateral" with one of its angles equal to 180º - in effect making it look like triangle

        self.d["test_yourself"] = _("Test yourself")
        self.d["Clock1"] = _("Clock")
        self.d["Read time"] = _("learn to read the time")
        self.d["Clock2"] = _("Clock")
        self.d["Set time"] = _("learn to set the clock")
        self.d["Set_clock"] = _("Set the clock to:")
        self.d["Set_clock_instr"] = _("Drag the clock hands to set the time")
        self.d["What time"] = _("What time is it?")
        self.d["close_confirm"] = _("Click again to exit")
        self.d["answer_enter"] = _("Type your answer and hit enter")

        #self.d["enable_untranslated"] = _("FAO: Translators - enable this to show untranslated languages (for testing):")
        #self.d["Fullscreen:"] = _("Fullscreen:")

        self.d["Time"] = _("Time")
        self.d["Play_w_clock"] = _("Turn the clock hands and see what happens.")

        self.d["lets_see_what_you_draw"] = _("Let's see what shapes you can draw")
        self.d["txt_only"] = _("Time in text version only")
        self.d["Clock0"] = _("How clock works?")
        self.d["Columnar addition"] = _("Columnar addition")
        self.d["Columnar subtraction"] = _("Columnar subtraction")
        self.d["Long multiplication"] = _("Long multiplication")
        self.d["Long division"] = _("Long division")
        self.d["borrow 10"] = _("borrow 10")
        self.d["carry"] = _("carry") #in columnar addition, ie. in case of 4 + 8 you write 2 under the column and carry 1
        self.d["demo start"] = _("Start >>")
        self.d["demo next eg"] = _("Next example >>")
        self.d["demo next step"] = _("Next step >>")
        self.d["demo write"] = _("write ") #used to show which digit of the result should be entered in a box, ie. "enter 5")
        self.d["Demonstration"] = _("Demonstration")
        self.d["DIY"] = _("Do it yourself")
        self.d["Ratio"] = _("Ratio")
        self.d["Working with large numbers"] = _("Working with large numbers")
        self.d["demo rewrite"] = _("rewrite ")
        self.d["demo rewrite"] = _("rewrite ")
        self.d["remainder"] = _("remainder")
        self.d["demo_result"] = _("result")
        self.d["TimeMatching"] = _("Time Matching")

        self.d["more red"] = _("Add some red")
        self.d["more green"] = _("Add some green")
        self.d["more blue"] = _("Add some blue")
        self.d["more cyan"] = _("Add some cyan")
        self.d["more magenta"] = _("Add some magenta")
        self.d["more yellow"] = _("Add some yellow")


        self.d["less red"] = _("Too much red")
        self.d["less green"] = _("Too much green")
        self.d["less blue"] = _("Too much blue")
        self.d["less cyan"] = _("Too much cyan")
        self.d["less magenta"] = _("Too much magenta")
        self.d["less yellow"] = _("Too much yellow")


        self.d["red is ok"] = _("red is spot on")
        self.d["green is ok"] = _("green is spot on")
        self.d["blue is ok"] = _("blue is spot on")
        self.d["cyan is ok"] = _("cyan is spot on")
        self.d["magenta is ok"] = _("magenta is spot on")
        self.d["yellow is ok"] = _("yellow is spot on")

        self.d["art4apps"] = _("Images from: http://www.art4apps.org/ - Art4Apps by Smart4Kids - Creative Commons License (CC BY-SA)")
        self.d["Word Builder - Animals"] = _("Word Builder - Animals")
        self.d["Word Builder - Sports"] = _("Word Builder - Sports")
        self.d["Word Builder - Body"] = _("Word Builder - Body")
        self.d["Word Builder - People"] = _("Word Builder - People")
        self.d["Word Builder - Actions"] = _("Word Builder - Actions")
        self.d["Word Builder - Constructions"] = _("Word Builder - Constructions")
        self.d["Word Builder - Nature"] = _("Word Builder - Nature")
        self.d["Word Builder - Jobs"] = _("Word Builder - Jobs")
        self.d["Word Builder - Clothes and Accessories"] = _("Word Builder - Clothes and Accessories")
        self.d["Word Builder - Fruits and Vegetables"] = _("Word Builder - Fruits and Vegetables")
        self.d["Word Builder - Transport"] = _("Word Builder - Transport")
        self.d["Word Builder - Food"] = _("Word Builder - Food")
        self.d["Complete the word"] = _("Complete the word")

        self.d["Do you want to exit the game?"] = _("Do you want to exit the game?")
        self.d["Do you want to log out of the game?"] = _("Do you want to  log out of the game?")
        self.d["Ready to go to the next level?"] = _("Ready to go to the next level?")

        #New as of pysiogame3
        self.d["Clock_cat"] = _("Clock")
        #self.d["Units of Time"] = _("Units of Time")
        #self.d["Time Calculations"] = _("Time Calculations")

        self.d["Achievements"] = _("Achievements")
        self.d["Learn to count"] = _("Learn to count")
        self.d["Addition"] = _("Addition")
        self.d["Subtraction"] = _("Subtraction")
        self.d["Multiplication"] = _("Multiplication")
        self.d["Division"] = _("Division")
        self.d["Fractions"] = _("Fractions")
        self.d["Decimals and Fractions"] = _("Decimals and Fractions")
        self.d["Decimals, fractions and percentages"] = _("Decimals, fractions and percentages")
        self.d["Decimals, fractions, ratios and percentages"] = _("Decimals, fractions, ratios and percentages")
        self.d["Shapes and Solids"] = _("Shapes and Solids")
        self.d["Nothing here yet..."] = _("Nothing here yet...")
        self.d["Translation Credits"] = _("Translation Credits")
        self.d["Level"] = _("Level")
        self.d["Build the following word using the letters below."] = _("Build the following word using the letters below.")
        self.d["Find solution"] = _("Find solution")
        self.d["Find missing number"] = _("Find missing number")
        self.d["Language arts"] = _("Language arts")
        self.d["Other"] = _("Other")


        """
        self.d["a4a_animals"] = [_("cow"), _("turkey"), _("shrimp"), _("wolf"), _("panther"), _("panda"), _("magpie"), _("clam"), _("pony"), _("mouse"), _("pug"), _("koala"), _("frog"), _("ladybug"), _("gorilla"), _("llama"), _("vulture"), _("hamster"), _("bird"), _("starfish"), _("crow"), _("parakeet"), _("caterpillar"), _("tiger"), _("hummingbird"), _("piranha"), _("pig"), _("scorpion"), _("fox"), _("leopard"), _("iguana"), _("dolphin"), _("bat"), _("chick"), _("crab"), _("hen"), _("wasp"), _("chameleon"), _("whale"), _("hedgehog"), _("fawn"), _("moose"), _("bee"), _("viper"), _("shrike"), _("donkey"), _("guinea pig"), _("sloth"), _("horse"), _("penguin"), _("otter"), _("bear"), _("zebra"), _("ostrich"), _("camel"), _("antelope"), _("lemur"), _("pigeon"), _("lama"), _("mole"), _("ray"), _("ram"), _("skunk"), _("jellyfish"), _("sheep"), _("shark"), _("kitten"), _("deer"), _("snail"), _("flamingo"), _("rabbit"), _("oyster"), _("beaver"), _("sparrow"), _("dove"), _("eagle"), _("beetle"), _("hippopotamus"), _("owl"), _("cobra"), _("salamander"), _("goose"), _("kangaroo"), _("dragonfly"), _("toad"), _("pelican"), _("squid"), _("lion cub"), _("jaguar"), _("duck"), _("lizard"), _("rhinoceros"), _("hyena"), _("ox"), _("peacock"), _("parrot"), _("elk"), _("alligator"), _("ant"), _("goat"), _("baby rabbit"), _("lion"), _("squirrel"), _("opossum"), _("chimp"), _("doe"), _("gopher"), _("elephant"), _("giraffe"), _("spider"), _("puppy"), _("jay"), _("seal"), _("rooster"), _("turtle"), _("bull"), _("cat"), _("lamb"), _("rat"), _("slug"), _("buffalo"), _("blackbird"), _("swan"), _("lobster"), _("dog"), _("mosquito"), _("snake"), _("chicken"), _("anteater")]
        self.d["a4a_sport"] = [_("judo"), _("pool"), _("ride"), _("stretch"), _("helmet"), _("ice skating"), _("walk"), _("ran"), _("run"), _("swim"), _("hop"), _("hike"), _("boxing"), _("hockey"), _("race"), _("throw"), _("skate"), _("win"), _("squat"), _("ski"), _("golf"), _("whistle"), _("torch"), _("sailing"), _("stand"), _("tennis"), _("jump"), _("rowing"), _("jog"), _("rope")]
        self.d["a4a_body"] = [_("teeth"), _("cheek"), _("ankle"), _("knee"), _("toe"), _("muscle"), _("mouth"), _("feet"), _("hand"), _("elbow"), _("hair"), _("eyelash"), _("beard"), _("belly button"), _("thumb"), _("breast"), _("nostril"), _("nose"), _("hip"), _("arm"), _("eyebrow"), _("fist"), _("neck"), _("wrist"), _("throat"), _("eye"), _("leg"), _("spine"), _("ear"), _("finger"), _("foot"), _("braid"), _("face"), _("back"), _("chin"), _("bottom"), _("thigh"), _("belly")]
        self.d["a4a_people"] = [_("girl"), _("male"), _("son"), _("mates"), _("friends"), _("baby"), _("child"), _("dad"), _("mom"), _("twin boys"), _("brothers"), _("man"), _("mother"), _("grandfather"), _("family"), _("female"), _("wife"), _("husband"), _("bride"), _("madam"), _("grandmother"), _("couple"), _("lad"), _("twin girls"), _("tribe"), _("boy"), _("sisters"), _("woman"), _("lady")]
        self.d["a4a_food"] = [_("candy"), _("sausage"), _("hamburger"), _("steak"), _("fudge"), _("doughnut"), _("coconut"), _("rice"), _("ice cream"), _("jelly"), _("yoghurt"), _("dessert"), _("pretzel"), _("peanut"), _("jam"), _("feast"), _("cookie"), _("bacon"), _("spice"), _("coffee"), _("pie"), _("lemonade"), _("chocolate"), _("water bottle"), _("lunch"), _("ice"), _("sugar"), _("sauce"), _("soup"), _("juice"), _("fries"), _("cake"), _("mashed potatoes"), _("tea"), _("bun"), _("cheese"), _("beef"), _("sandwich"), _("slice"), _("sprinkle"), _("pizza"), _("flour"), _("gum"), _("spaghetti"), _("roast"), _("drink"), _("stew"), _("spread"), _("meat"), _("milk"), _("meal"), _("corn"), _("bread"), _("walnut"), _("egg"), _("hot dog"), _("ham")]
        self.d["a4a_clothes_n_accessories"] = [_("jewellery"), _("sock"), _("jacket"), _("heel"), _("smock"), _("shorts"), _("pocket"), _("necklace"), _("sweatshirt"), _("uniform"), _("raincoat"), _("trousers"), _("sunglasses"), _("coat"), _("pullover"), _("shirt"), _("sandals"), _("suit"), _("pyjamas"), _("skirt"), _("zip"), _("shoes"), _("jewel"), _("tie"), _("slippers"), _("gloves"), _("hat"), _("sleeve"), _("cap"), _("swimming suit"), _("sneaker"), _("vest"), _("glasses"), _("shoelace"), _("patch"), _("scarf"), _("shoe"), _("button"), _("dress"), _("sash"), _("shoe sole"), _("robe"), _("pants"), _("kimono"), _("overalls")]
        self.d["a4a_actions"] = [_("lick"), _("slam"), _("beg"), _("fell"), _("scratch"), _("touch"), _("sniff"), _("see"), _("climb"), _("dig"), _("howl"), _("sleep"), _("explore"), _("draw"), _("hug"), _("teach"), _("nap"), _("clay"), _("catch"), _("clap"), _("cry"), _("sing"), _("meet"), _("sell"), _("peck"), _("beat"), _("kneel"), _("find"), _("dance"), _("cough"), _("cut"), _("think"), _("bark"), _("speak"), _("cheer"), _("bake"), _("write"), _("punch"), _("strum"), _("study"), _("plow"), _("dream"), _("post"), _("dive"), _("whisper"), _("sob"), _("shake"), _("feed"), _("crawl"), _("camp"), _("spill"), _("clean"), _("scream"), _("tear"), _("float"), _("pull"), _("ate"), _("kiss"), _("sit"), _("hatch"), _("blink"), _("hear"), _("smooch"), _("play"), _("wash"), _("chat"), _("drive"), _("drink"), _("fly"), _("juggle"), _("bit"), _("sweep"), _("look"), _("knit"), _("lift"), _("fetch"), _("read"), _("croak"), _("stare"), _("eat")]
        self.d["a4a_construction"] = [_("lighthouse"), _("door"), _("circus"), _("church"), _("kennel"), _("temple"), _("smoke"), _("chimney"), _("brick"), _("well"), _("street"), _("castle"), _("store"), _("staircase"), _("school"), _("farm"), _("bridge"), _("dam"), _("pyramid"), _("barn"), _("mill"), _("window"), _("cabin"), _("step"), _("shop"), _("shed"), _("roof"), _("steeple"), _("garage"), _("mosque"), _("hospital"), _("tent"), _("house"), _("wall"), _("bank"), _("shutter"), _("hut")]
        self.d["a4a_nature"] = [_("land"), _("cliff"), _("hill"), _("canyon"), _("rock"), _("sea"), _("lake"), _("coast"), _("shore"), _("mountain"), _("pond"), _("peak"), _("lava"), _("cave"), _("dune"), _("island"), _("forest"), _("desert"), _("iceberg")]
        self.d["a4a_jobs"] = [_("clown"), _("engineer"), _("priest"), _("vet"), _("judge"), _("chef"), _("athlete"), _("librarian"), _("juggler"), _("police"), _("plumber"), _("badge"), _("queen"), _("farmer"), _("magic"), _("knight"), _("doctor"), _("bricklayer"), _("cleaner"), _("teacher"), _("hunter"), _("soldier"), _("musician"), _("lawyer"), _("fisherman"), _("princess"), _("fireman"), _("nun"), _("chief"), _("pirate"), _("cowboy"), _("electrician"), _("nurse"), _("king"), _("president"), _("office"), _("carpenter"), _("jockey"), _("worker"), _("mechanic"), _("pilot"), _("actor"), _("cook"), _("student"), _("butcher"), _("accountant"), _("prince"), _("pope"), _("sailor"), _("boxer"), _("ballet"), _("coach"), _("astronaut"), _("painter"), _("anaesthesiologist"), _("scientist")]
        self.d["a4a_fruit_n_veg"] = [_("carrot"), _("blackberries"), _("celery"), _("turnip"), _("cacao"), _("peach"), _("melon"), _("grapefruit"), _("broccoli"), _("grapes"), _("spinach"), _("fig"), _("kernel"), _("radish"), _("tomato"), _("kiwi"), _("asparagus"), _("olives"), _("cucumbers"), _("beans"), _("strawberry"), _("peppers"), _("raspberry"), _("apricot"), _("potatoes"), _("peas"), _("cabbage"), _("cherries"), _("squash"), _("blueberries"), _("pear"), _("orange"), _("pumpkin"), _("avocado"), _("garlic"), _("onion"), _("apple"), _("lime"), _("cauliflower"), _("mango"), _("lettuce"), _("lemon"), _("aubergine"), _("artichokes"), _("plums"), _("leek"), _("bananas"), _("papaya")]
        self.d["a4a_transport"] = [_("sail"), _("taxi"), _("car"), _("bike"), _("raft"), _("pedal"), _("bus"), _("handlebar"), _("boat"), _("truck"), _("sleigh"), _("carpet"), _("motorcycle"), _("train"), _("ship"), _("van"), _("canoe"), _("rocket"), _("mast"), _("sledge"), _("bicycle")]
        """
