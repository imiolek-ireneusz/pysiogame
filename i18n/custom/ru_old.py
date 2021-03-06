# -*- coding: utf-8 -*-

# Translated by Anton Kayukov (Антон Каюков), Alexey Loginov (Алексей Логинов)

# FAO Translators:
# First of all thank you for your interest in translating this game,
# I will be grateful if you could share it with the community -
# if possible please send it back to my email, and I'll add it to the next version.

# The translation does not have to be exact as long as it makes sense and fits in its location
# (if it doesn't I'll try to either make the font smaller or make the area wider - where possible).
# The colour names in other languages than English are already in smaller font.

d = dict()  # messages for display
dp = dict()  # messages with pronunciation exceptions - this dictionary will override entries in a copy of d

d["local_kbrd"] = "Русскими буквами"
d[
    "Clock0 - Russian official time"] = "Научитесь читать официальное русское время"  # Learn to read Russian official time
d["Russian official - subtitle"] = ""

d["Clock2 - Russian official time"] = "Официальное русское время"  # Russian official time
d["Russian official - txt_only"] = "Протестируйте сами себя"  # test yourself

numbers = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
           "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
           "девятнадцать", "двадцать", "двадцать один", "двадцать два", "двадцать три", "двадцать четыре",
           "двадцать пять", "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять"]
numbers2090 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

# dp['abc_flashcards_word_sequence'] = ['Автобус', 'Банка', 'Виноград','Гитара','Дом','Ель', 'Ёж', 'Жеребец', 'Зебра',  'Иглу', 'Йога','Кошка','Лев', 'Муравей', 'Ночь', 'Обувь', 'Попугай', 'Рыба', 'Слон','Томат','Утка','Филин', 'Хлеб', 'Цветок', 'Чайник', 'Шлюпка', 'Щука','Съёмка', 'Мышь', 'Нить', 'Электричка', 'Юбка', 'Яхта']
d['abc_flashcards_word_sequence'] = ['<1>А<2>втобус', '<1>Б<2>анка', '<1>В<2>иноград', '<1>Г<2>итара', '<1>Д<2>ом',
                                     '<1>Е<2>ль', '<1>Ё<2>ж', '<1>Ж<2>еребец', '<1>З<2>ебра', '<1>И<2>глу',
                                     '<1>Й<2>ога', '<1>К<2>ош<1>к<2>а', '<1>Л<2>ев', '<1>М<2>уравей', '<1>Н<2>очь',
                                     '<1>О<2>бувь', '<1>П<2>о<1>п<2>угай', '<1>Р<2>ыба', '<1>С<2>лон', '<1>Т<2>ома<1>т',
                                     '<1>У<2>тка', '<1>Ф<2>илин', '<1>Х<2>леб', '<1>Ц<2>веток', '<1>Ч<2>айник',
                                     '<1>Ш<2>люпка', '<1>Щ<2>ука', '<2>С<1>ъ<2>ёмка', '<2>М<1>ы<2>шь', '<2>Нит<1>ь',
                                     '<1>Э<2>лектричка', '<1>Ю<2>бка', '<1>Я<2>хта']
d['abc_flashcards_frame_sequence'] = [77, 9, 6, 28, 7, 31, 29, 45, 25, 8, 32, 2, 11, 0, 54, 60, 15, 5, 4, 33, 3, 14, 35,
                                      69, 19, 1, 38, 39, 12, 24, 63, 41, 66]

# alphabet ru: - 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' & 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_lc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
               'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet_uc = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
               'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
# correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['-']
accents_uc = []


def n2txt(n, twoliner=False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbers[n - 1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090[(n // 10) - 2]
        if m == 0:
            return tens
        elif m > 0:
            ones = numbers[m - 1]
            if twoliner:
                return [tens, ones]
            else:
                return tens + " " + ones
    elif n == 0:
        return "ноль"
    elif n == 100:
        return "сто"
    return ""


# TIME FOR DISPLAY
mt1 = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
       "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
       "девятнадцать", "двадцать", "двадцать одна", "двадцать две", "двадцать три", "двадцать четыре", "двадцать пять",
       "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять", "тридцать", "тридцать одна",
       "тридцать две", "тридцать три", "тридцать четыре", "тридцать пять", "тридцать шесть", "тридцать семь",
       "тридцать восемь", "тридцать девять"]
mt2 = ["одной", "двух", "трёх", "четырёх", "пяти", "шести", "семи", "восьми", "девяти", "десяти", "одиннадцати",
       "двенадцати", "тринадцати", "четырнадцати", "пятнадцати", "шестнадцати", "семнадцати", "восемнадцати",
       "девятнадцати", "двадцати", "двадцати одной", "двадцати двух", "двадцати трёх", "двадцати четырёх",
       "двадцати пяти", "двадцати шести", "двадцати семи", "двадцати восьми", "двадцати девяти"]

ht1 = ["час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
       "двенадцать"]
ht2 = ["первого", "второго", "третьего", "четвёртого", "пятого", "шестого", "седьмого", "восьмого", "девятого",
       "десятого", "одиннадцатого", "двенадцатого"]


def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. six fifty five - for 6:55'
    if m > 0:
        if h == 12:
            h = 1
        else:
            h += 1

    if m == 0:
        if h == 1:
            return "один час"
        elif h < 5:
            return "%s часа" % ht1[h - 1]
        else:
            return "%s часов" % ht1[h - 1]
    elif m == 15:
        return "четверть %s" % ht2[h - 1]
    elif m == 20:
        return "%s минут %s" % (mt1[m - 1], ht2[h - 1])
    elif m in [1, 21]:
        return "%s минута %s" % (mt1[m - 1], ht2[h - 1])
    elif m in [2, 3, 4, 22, 23, 24]:
        return "%s минуты %s" % (mt1[m - 1], ht2[h - 1])
    elif m < 30:
        return "%s минут %s" % (mt1[m - 1], ht2[h - 1])
    elif m == 30:
        return "половина %s" % ht2[h - 1]
    elif m == 39:
        return "без двадцати одной минуты %s" % ht1[h - 1]
    elif m == 40:
        return "без %s минут %s" % (mt2[60 - m - 1], ht1[h - 1])
    elif m == 45:
        return "без четверти %s" % ht1[h - 1]
    elif m == 59:
        return "без одной минуты %s" % ht1[h - 1]
    elif m > 30:
        return "без %s минут %s" % (mt2[60 - m - 1], ht1[h - 1])
    return ""


def time2officialstr(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'

    # get the right "suffix" for hour
    if h == 1:
        sf = "час"
    elif h < 5:
        sf = "часа"
    else:
        sf = "часов"

    if m == 0:
        return "%s %s" % (numbers[h - 1], sf)
    elif m == 1:
        return "%s %s одна минута" % (numbers[h - 1], sf)
    elif m in [21, 31, 41, 51]:
        return "%s %s %s одна минута" % (numbers[h - 1], sf, n2txt(m - 1))
    elif m == 2:
        return "%s %s две минуты" % (numbers[h - 1], sf)
    elif m in [22, 32, 42, 52]:
        return "%s %s %s две минуты" % (numbers[h - 1], sf, n2txt(m - 2))
    elif m in [3, 4, 23, 24, 33, 34, 43, 44, 53, 54]:
        return "%s %s %s минуты" % (numbers[h - 1], sf, n2txt(m))
    else:
        return "%s %s %s минут" % (numbers[h - 1], sf, n2txt(m))
    return ""


# TIME FOR SPEAKER
spkmt1 = ["одна", "две", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
          "20", "20 одна", "20 две", "23", "24", "25", "26", "27", "28", "29", "30", "30 одна", "30 две", "33", "34",
          "35", "36", "37", "38", "39"]
spkmt2 = ["одной", "двух", "трёх", "четырёх", "пяти", "шести", "семи", "вось-ми", "девя-ти", "десяти", "1-надца-ти",
          "две-надца-ти", "три-надца-ти", "четыр-надца-ти", "пят-надца-ти", "шест-надца-ти", "сем-надца-ти",
          "восем-надца-ти", "девят-надца-ти", "двадца-ти", "двадца-ти одной", "двадца-ти двух", "двадца-ти трёх",
          "двадца-ти четырёх", "двадца-ти пяти", "двадца-ти шести", "двадца-ти семи", "двадца-ти вось-ми",
          "двадца-ти девя-ти"]

spkht1 = ["час", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
spkht2 = ["пер-во-во", "второго", "треть-его", "четвёртого", "пя-то-во", "шестого", "седьмого", "восьмого", "девятого",
          "десятого", "1-надца-того", "две-надца-того"]

spknumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
              "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]


def time2spk(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string but in exception format for espeak Russian language'
    if m > 0:
        if h == 12:
            h = 1
        else:
            h += 1

    if m == 0:
        if h == 1:
            return "1 час"
        elif h < 5:
            return "%s ча-са" % spkht1[h - 1]
        else:
            return "%s ча-сов" % spkht1[h - 1]
    elif m == 15:
        return "чет-верть %s" % spkht2[h - 1]
    elif m == 20:
        return "%s минут %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m in [1, 21]:
        return "%s минута %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m in [2, 3, 4, 22, 23, 24]:
        return "%s минуты %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m < 30:
        return "%s минут %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m == 30:
        return "половина %s" % spkht2[h - 1]
    elif m == 39:
        return "без двад-ца-ти одной минуты %s" % spkht1[h - 1]
    elif m == 40:
        return "без %s минут %s" % (spkmt2[60 - m - 1], spkht1[h - 1])
    elif m == 45:
        return "без четвер-ти %s" % spkht1[h - 1]
    elif m == 59:
        return "без од-ной минуты %s" % spkht1[h - 1]
    elif m > 30:
        return "без %s минут %s" % (spkmt2[60 - m - 1], spkht1[h - 1])
    return ""


def time2officialspk(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'

    # get the right "suffix" for hour
    if h == 1:
        sf = "час"
    elif h < 5:
        sf = "ча-са"
    else:
        sf = "ча-сов"

    if m == 0:
        return "%s %s" % (spknumbers[h - 1], sf)
    elif m == 1:
        return "%s %s одна минута" % (spknumbers[h - 1], sf)
    elif m in [21, 31, 41, 51]:
        return "%s %s %d-одна минута" % (spknumbers[h - 1], sf, m - 1)
    elif m == 2:
        return "%s %s две минуты" % (spknumbers[h - 1], sf)
    elif m in [22, 32, 42, 52]:
        return "%s %s %d-две минуты" % (spknumbers[h - 1], sf, m - 2)
    elif m in [3, 4, 23, 24, 33, 34, 43, 44, 53, 54]:
        return "%s %s %d минуты" % (spknumbers[h - 1], sf, m)
    else:
        return "%s %s %d минут" % (spknumbers[h - 1], sf, m)
    return ""


d["a4a_animals"] = ["cow", "turkey", "shrimp", "wolf", "panther", "panda", "magpie", "clam", "pony", "mouse", "pug",
                    "koala", "frog", "ladybug", "gorilla", "llama", "vulture", "hamster", "bird", "starfish", "crow",
                    "parakeet", "caterpillar", "tiger", "hummingbird", "piranha", "pig", "scorpion", "fox", "leopard",
                    "iguana", "dolphin", "bat", "chick", "crab", "hen", "wasp", "chameleon", "whale", "hedgehog",
                    "fawn", "moose", "bee", "viper", "shrike", "donkey", "guinea pig", "sloth", "horse", "penguin",
                    "otter", "bear", "zebra", "ostrich", "camel", "antelope", "lemur", "pigeon", "lama", "mole", "ray",
                    "ram", "skunk", "jellyfish", "sheep", "shark", "kitten", "deer", "snail", "flamingo", "rabbit",
                    "oyster", "beaver", "sparrow", "dove", "eagle", "beetle", "hippopotamus", "owl", "cobra",
                    "salamander", "goose", "kangaroo", "dragonfly", "toad", "pelican", "squid", "lion cub", "jaguar",
                    "duck", "lizard", "rhinoceros", "hyena", "ox", "peacock", "parrot", "elk", "alligator", "ant",
                    "goat", "baby rabbit", "lion", "squirrel", "opossum", "chimp", "doe", "gopher", "elephant",
                    "giraffe", "spider", "puppy", "jay", "seal", "rooster", "turtle", "bull", "cat", "lamb", "rat",
                    "slug", "buffalo", "blackbird", "swan", "lobster", "dog", "mosquito", "snake", "chicken",
                    "anteater"]
d["a4a_sport"] = ["judo", "pool", "ride", "stretch", "helmet", "ice skating", "walk", "ran", "run", "swim", "hop",
                  "hike", "boxing", "hockey", "race", "throw", "skate", "win", "squat", "ski", "golf", "whistle",
                  "torch", "sailing", "stand", "tennis", "jump", "rowing", "jog", "rope"]
d["a4a_body"] = ["teeth", "cheek", "ankle", "knee", "toe", "muscle", "mouth", "feet", "hand", "elbow", "hair",
                 "eyelash", "beard", "belly button", "thumb", "breast", "nostril", "nose", "hip", "arm", "eyebrow",
                 "fist", "neck", "wrist", "throat", "eye", "leg", "spine", "ear", "finger", "foot", "braid", "face",
                 "back", "chin", "bottom", "thigh", "belly"]
d["a4a_people"] = ["girl", "male", "son", "mates", "friends", "baby", "child", "dad", "mom", "twin boys", "brothers",
                   "man", "mother", "grandfather", "family", "female", "wife", "husband", "bride", "madam",
                   "grandmother", "couple", "lad", "twin girls", "tribe", "boy", "sisters", "woman", "lady"]
d["a4a_food"] = ["candy", "sausage", "hamburger", "steak", "fudge", "doughnut", "coconut", "rice", "ice cream", "jelly",
                 "yoghurt", "dessert", "pretzel", "peanut", "jam", "feast", "cookie", "bacon", "spice", "coffee", "pie",
                 "lemonade", "chocolate", "water bottle", "lunch", "ice", "sugar", "sauce", "soup", "juice", "fries",
                 "cake", "mashed potatoes", "tea", "bun", "cheese", "beef", "sandwich", "slice", "sprinkle", "pizza",
                 "flour", "gum", "spaghetti", "roast", "drink", "stew", "spread", "meat", "milk", "meal", "corn",
                 "bread", "walnut", "egg", "hot dog", "ham"]
d["a4a_clothes_n_accessories"] = ["jewellery", "sock", "jacket", "heel", "smock", "shorts", "pocket", "necklace",
                                  "sweatshirt", "uniform", "raincoat", "trousers", "sunglasses", "coat", "pullover",
                                  "shirt", "sandals", "suit", "pyjamas", "skirt", "zip", "shoes", "jewel", "tie",
                                  "slippers", "gloves", "hat", "sleeve", "cap", "swimming suit", "trainer", "vest",
                                  "glasses", "shoelace", "patch", "scarf", "shoe", "button", "dress", "sash",
                                  "shoe sole", "robe", "pants", "kimono", "overalls"]
d["a4a_actions"] = ["lick", "slam", "beg", "fell", "scratch", "touch", "sniff", "see", "climb", "dig", "howl", "sleep",
                    "explore", "draw", "hug", "teach", "nap", "clay", "catch", "clap", "cry", "sing", "meet", "sell",
                    "peck", "beat", "kneel", "find", "dance", "cough", "cut", "think", "bark", "speak", "cheer", "bake",
                    "write", "punch", "strum", "study", "plow", "dream", "post", "dive", "whisper", "sob", "shake",
                    "feed", "crawl", "camp", "spill", "clean", "scream", "tear", "float", "pull", "ate", "kiss", "sit",
                    "hatch", "blink", "hear", "smooch", "play", "wash", "chat", "drive", "drink", "fly", "juggle",
                    "bit", "sweep", "look", "knit", "lift", "fetch", "read", "croak", "stare", "eat"]
d["a4a_construction"] = ["lighthouse", "door", "circus", "church", "kennel", "temple", "smoke", "chimney", "brick",
                         "well", "street", "castle", "store", "staircase", "school", "farm", "bridge", "dam", "pyramid",
                         "barn", "mill", "window", "cabin", "step", "shop", "shed", "roof", "steeple", "garage",
                         "mosque", "hospital", "tent", "house", "wall", "bank", "shutter", "hut"]
d["a4a_nature"] = ["land", "cliff", "hill", "canyon", "rock", "sea", "lake", "coast", "shore", "mountain", "pond",
                   "peak", "lava", "cave", "dune", "island", "forest", "desert", "iceberg"]
d["a4a_jobs"] = ["clown", "engineer", "priest", "vet", "judge", "chef", "athlete", "librarian", "juggler", "police",
                 "plumber", "badge", "queen", "farmer", "magic", "knight", "doctor", "bricklayer", "cleaner", "teacher",
                 "hunter", "soldier", "musician", "lawyer", "fisherman", "princess", "fireman", "nun", "chief",
                 "pirate", "cowboy", "electrician", "nurse", "king", "president", "office", "carpenter", "jockey",
                 "worker", "mechanic", "pilot", "actor", "cook", "student", "butcher", "accountant", "prince", "pope",
                 "sailor", "boxer", "ballet", "coach", "astronaut", "painter", "anaesthesiologist", "scientist"]
d["a4a_fruit_n_veg"] = ["carrot", "blackberries", "celery", "turnip", "cacao", "peach", "melon", "grapefruit",
                        "broccoli", "grapes", "spinach", "fig", "kernel", "radish", "tomato", "kiwi", "asparagus",
                        "olives", "cucumbers", "beans", "strawberry", "peppers", "raspberry", "apricot", "potatoes",
                        "peas", "cabbage", "cherries", "squash", "blueberries", "pear", "orange", "pumpkin", "avocado",
                        "garlic", "onion", "apple", "lime", "cauliflower", "mango", "lettuce", "lemon", "aubergine",
                        "artichokes", "plums", "leek", "bananas", "papaya"]
d["a4a_transport"] = ["sail", "taxi", "car", "bike", "raft", "pedal", "bus", "handlebar", "boat", "truck", "sleigh",
                      "carpet", "motorcycle", "train", "ship", "van", "canoe", "rocket", "mast", "sledge", "bicycle"]

dp["Welcome back."] = "Доб-ро по-жа-ловать в иг-ру."

dp['abc_flashcards_word_sequence'] = ['Автобус', 'Банка', 'Виноград', 'Гитара', 'Дом', 'Ель', 'Ёж', 'Жеребец', 'Зебра',
                                      'Иглу', 'Йога', 'Кошка', 'Лев', 'Муравей', 'Ночь', 'Обувь', 'Попугай', 'Рыба',
                                      'Слон', 'Томат', 'Утка', 'Филин', 'Хлеб', 'Цветок', 'Чайник', 'Шлюпка', 'Щука',
                                      'Съёмка', 'Мышь', 'Нить', 'Электричка', 'Юбка', 'Яхта']
dp["shape_names"] = ["Равносторонний треугольник", "Равнобедренный треугольник", "Тупоугольный треугольник",
                     "Прямоугольный треугольник", "Остроугольный треугольник", "Квадрат", "Прямоугольник",
                     "Правильная трапеция", "Равнобедренная трапеция", "Ромб", "Пара-лле-ло-грамм", "Пятиугольник",
                     "Шестиугольник", "Круг", "Эллипс"]
dp["solid_names"] = ["Куб", "Квадратная призма", "Треугольная призма", "Квадратная пирамида", "Треугольная пирамида",
                     "Сфера", "Цилиндр", "Конус", "Тор"]

dp["fruit"] = ["зе-лё-ное яб-ло-ко", "крас-ное яб-ло-ко", "клубника", "груша", "апель-син", "луковица", "томат",
               "ли-мон", "вишня", "пе--рец", "мор-ковь", "ба-нан", "ар-буз"]

# game instructions
dp[
    "Drag the slider"] = "Перетащите ползунок вверх или вниз так, чтобы правильный знак оказался в красном квадрате."  # Drag the slider up or down so that the right sign is in the red square.
# dp["Take your sheep"] = "Приве-ди-те овцу к ос-таль-но-му стаду." #Take your sheep to the rest of the herd.

dp[
    "Check the shopping list"] = "Проверьте список покупок и перетащите все необходи-мые предметы в корзину."  # Check the shopping list and drag all needed items into the basket.
dp[
    "Drag lt2"] = "Перетащите 1 из меньше, больше или ра-вно в красный квадрат."  # Drag one of the greater, lesser or equal to the red square.
dp[
    "Re-arrange right"] = "Переставьте цифры, чтобы они были в правильном порядке"  # Re-arrange the above numbers so they are in the right order
dp["Complete abc"] = "Заполните алфавит с помощью букв."  # Complete the abc using the letters above.
dp["Write a word:"] = "Напишите слово:"  # Write a word:
dp[
    "Find and separate"] = "Найдите и отделите чётные числа от нечётных чисел в указанной последовательна-сти."  # Find and separate the Even Numbers from the Odd Numbers in the above series.
dp[
    "Re-arrange alphabetical"] = "Переставьте буквы, чтобы они были в алфавитном порядке."  # Re-arrange the above letters so they are in the alphabetical order.
dp[
    "Re-arrange ascending"] = "Переставьте цифры, чтобы они были в порядке возрастания."  # Re-arrange the above numbers so they are in the ascending order.

# dp["Please try again."] = "Пожалуйста, попробуйте ещё раз."#no longer used
# dp["Sorry! It is wrong."] = "Извините! Это неправильно." #no longer uses
dp["Perfect! Task solved!"] = "Великолепно! Задача решена!"
dp["work harder"] = "В следующий раз постарайтесь ра-бо-тать лучше."

# level_controller
dp["Game Over!"] = "Игра проиграна!"
dp["Congratulations! Game Completed."] = "Поздравляем! Вы выполнили все задачи в этой игре."
dp["Great job!"] = ["Отличная работа", "Велико-лепно", "Потрясающе", "Фантастическая работа",
                    "Мо-ло-дец"]  # ["Great job!","Perfect!","Awesome!","Fantastic job!","Well done!"]
dp["Perfect! Level completed!"] = "Великолепно! Уровень завершён!"

dp["Perfect!"] = "Велико-лепно"  # Perfect!

# game specific labels:
dp["area:"] = "пло-щадь:"  # area:
dp["circumference:"] = "окру--жность::"  # circumference:
dp["perimeter:"] = "периметр:"
dp["surface area:"] = "пло-щадь поверхности:"  # surface area:
dp["volume:"] = "объём"  # volume:
dp["divided by"] = "делённое на"  # divided by
dp["multiplied by"] = "умножен-ное на"
dp["equals"] = "ра-вно"  # equals
# dp["Shopping List"] = "Список поку-пок" #Shopping List
dp["Even"] = "Чётные"  # Even
dp["Odd"] = "Нечётные"  # Odd

dp["white"] = "Белый"  # "white"
dp["black"] = "Чёрный"  # "black"
dp["grey"] = "Серый"  # "grey"
dp["red"] = "Красный"  # "red"
dp["orange"] = "Оран-же-вый"  # "orange"
dp["yellow"] = "Жёлтый"  # "yellow"
dp["olive"] = "Оли-вковый"  # "olive"
dp["green"] = "Зелёный"  # "green"
dp["sea green"] = "Мор-ской вол-ны"  # "sea green"
dp["teal"] = "Сине-зелёный"  # "teal"
dp["blue"] = "Синий"  # "blue"
dp["navy"] = "Тёмно-синий"  # "navy"
dp["purple"] = "Фиолетовый"  # "purple"
# dp["violet"] = "Лиловый" #"violet"
dp["magenta"] = "Пурпурный"  # "magenta"
dp["indigo"] = "Индиго"  # "indigo"
dp["pink"] = "Ро-зо-вый"  # "pink"
dp["maroon"] = "Бордовый"  # maroon
dp["brown"] = "Коричневый"  # brown
dp["aqua"] = "Го-лу-бой"  # aqua
dp["lime"] = "Лайм"  # lime

dp["more red"] = "ещё красного"
dp["more green"] = "ещё зелёного"
dp["more blue"] = "ещё синего"
dp["more cyan"] = "ещё го-лу-бого"
dp["more magenta"] = "ещё пурпурного"
dp["more yellow"] = "ещё жёлтого"

dp["less red"] = "поменьше красного"
dp["less green"] = "поменьше зелёного"
dp["less blue"] = "поменьше синего"
dp["less cyan"] = "поменьше го-лу-бого"
dp["less magenta"] = "поменьше пурпурного"
dp["less yellow"] = "поменьше жёлтого"

dp["red is ok"] = "красного нормально"
dp["green is ok"] = "зелёного нормально"
dp["blue is ok"] = "синего нормально"
dp["cyan is ok"] = "го-лу-бого нормально"
dp["magenta is ok"] = "пурпурного нормально"
dp["yellow is ok"] = "жёлтого нормально"

dp[
    "Fract instr0"] = "Устано-вите соответствие дро-бей справа и дро-бей слева"  # Match fraction charts on the right to the ones on the left
dp[
    "Fract instr1"] = "Устано-вите соответствие дро-бей справа дро-бям слева"  # [Match fraction charts and fractions on the right","to the fraction charts on the left"]
dp[
    "Fract instr2"] = "Устано-вите соответствие дро-бей справа дро-бям слева"  # Match fraction charts to the fractions on the left
dp[
    "Fract instr3"] = "Устано-вите соответствие дро-бей и десятичных дро-бей справа их процентному представлению слева"  # ["Match fraction charts, fractions and decimal fractions on the right","to their percentage representations"]
dp[
    "Fract instr4"] = "Устано-вите соответствие отношений слева отношениям справа. Отношения показаны как отношения цвет-ных час-тей к белым час-тям"  # ["Match charts to the ratios on the left","Ratios are expressed as ratio of coloured pieces to white pieces"]
