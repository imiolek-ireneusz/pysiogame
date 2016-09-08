# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

d = dict()
dp = dict() # messages with pronunciation exceptions - this dictionary will override entries in a copy of d

d["local_kbrd"] = "Ελληνικά γράμματα"
numbers = ['ένα', 'δύο', 'τρία', 'τέσσερα', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα', 'δεκατρία', 'δεκατέσσερα', 'δεκαπέντε', 'δεκαέξι', 'δεκαεπτά', 'δεκαοκτώ', 'δεκαεννέα', 'είκοσι', 'είκοσι ένα', 'είκοσι δύο', 'είκοσι τρία', 'είκοσι τέσσερα', 'είκοσι πέντε', 'είκοσι έξι', 'είκοσι επτά', 'είκοσι οκτώ', 'είκοσι εννέα']
numbers2090 = ['είκοσι','τριάντα','σαράντα','πενήντα','εξήντα','εβδομήντα','ογδόντα','ενενήντα']

dp['abc_flashcards_word_sequence'] = ['Άλογο', 'Βάρκα', 'Γάτα', 'Δέντρο', 'Ελέφαντας', 'Ζέβρα', 'Ήλιος', 'Θάμνος', 'Ιπποπόταμος', 'Καμηλοπάρδαλη', 'Λουλούδια', 'Μήλο', 'Ντομάτα', 'Ξυλόφωνο', 'Ομπρέλα', 'Πάπια', 'Ρούχα', 'Σπίτι', 'Τσαγιέρα', 'Ύπνος', 'Φορτηγό', 'Χιμπατζής', 'Ψάρι', 'Ώρα']
d['abc_flashcards_word_sequence'] = ['<1>Ά<2>λογο', '<1>Β<2>άρκα', '<1>Γ<2>άτα', '<1>Δ<2>έντρο', '<1>Ε<2>λ<1>έ<2>φαντας', '<1>Ζ<2>έβρα', '<1>Ή<2>λιος', '<1>Θ<2>άμνος', '<1>Ι<2>πποπόταμος', '<1>Κ<2>αμηλοπάρδαλη', '<1>Λ<2>ου<1>λ<2>ούδια', '<1>Μ<2>ήλο', '<1>Ν<2>τομάτα', '<1>Ξ<2>υλόφωνο', '<1>Ο<2>μπρέλα', '<1>Π<2>ά<1>π<2>ια', '<1>Ρ<2>ούχα', '<1>Σ<2>πίτι', '<1>Τ<2>σαγιέρα', '<1>Ύ<2>πνος', '<1>Φ<2>ορτηγό', '<1>Χ<2>ιμπατζής', '<1>Ψ<2>άρι', '<1>Ώ<2>ρα']

d['abc_flashcards_frame_sequence'] = [45,1,2,31,4,25,18,46,47,30,36,42,33,23,20,3,48,7,19,49,50,37,5,51]

#alphabet gr
alphabet_lc = ['α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ', 'λ', 'μ', 'ν', 'ξ', 'ο', 'π', 'ρ', 'σ', 'τ', 'υ', 'φ', 'χ', 'ψ', 'ω']
alphabet_uc = ['Α', 'Β', 'Γ', 'Δ', 'Ε', 'Ζ', 'Η', 'Θ', 'Ι', 'Κ', 'Λ', 'Μ', 'Ν', 'Ξ', 'Ο', 'Π', 'Ρ', 'Σ', 'Τ', 'Υ', 'Φ', 'Χ', 'Ψ', 'Ω']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['-','ς','ά', 'έ', 'ή', 'ί','ϊ', 'ό', 'ύ', 'ώ']
accents_uc = ['Ά', 'Έ', 'Ή', 'Ί', 'Ϊ', 'Ό', 'Ύ', 'Ώ']

def n2txt(n, twoliner = False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbers[n-1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090[(n//10)-2]
        if m == 0:
            return tens
        elif m > 0:
            ones = numbers[m-1]
            if twoliner:
                return [tens, ones]
            else:
                return tens + " " + ones
    
    elif n == 0: return "μηδέν"
    elif n == 100: return "εκατό"
    return ""

hrs = ['μία', 'δύο', 'τρεις', 'τέσσερις', 'πέντε', 'έξι', 'επτά', 'οκτώ', 'εννέα', 'δέκα', 'έντεκα', 'δώδεκα']

def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if m == 0: return "%s ακριβώς" % hrs[h-1]
    elif m == 1: return "%s και ένα λεπτό" % hrs[h-1]
    elif m == 15: return "%s και τέταρτο" % hrs[h-1]
    elif m == 30: return "%s και μισή" % hrs[h-1]
    elif m == 45: return "%s παρά τέταρτο" % hrs[h-1]
    elif m == 59: return "%s παρά ένα λεπτό" % hrs[h-1]
    elif m < 30: return "%s και %s" % (hrs[h-1], n2txt(m))
    elif m > 30: return "%s παρά %s" % (hrs[h-1], n2txt(60-m))
    return ""
     
d["a4a_animals"] = ["cow", "turkey", "shrimp", "wolf", "panther", "panda", "magpie", "clam", "pony", "mouse", "pug", "koala", "frog", "ladybug", "gorilla", "llama", "vulture", "hamster", "bird", "starfish", "crow", "parakeet", "caterpillar", "tiger", "hummingbird", "piranha", "pig", "scorpion", "fox", "leopard", "iguana", "dolphin", "bat", "chick", "crab", "hen", "wasp", "chameleon", "whale", "hedgehog", "fawn", "moose", "bee", "viper", "shrike", "donkey", "guinea pig", "sloth", "horse", "penguin", "otter", "bear", "zebra", "ostrich", "camel", "antelope", "lemur", "pigeon", "lama", "mole", "ray", "ram", "skunk", "jellyfish", "sheep", "shark", "kitten", "deer", "snail", "flamingo", "rabbit", "oyster", "beaver", "sparrow", "dove", "eagle", "beetle", "hippopotamus", "owl", "cobra", "salamander", "goose", "kangaroo", "dragonfly", "toad", "pelican", "squid", "lion cub", "jaguar", "duck", "lizard", "rhinoceros", "hyena", "ox", "peacock", "parrot", "elk", "alligator", "ant", "goat", "baby rabbit", "lion", "squirrel", "opossum", "chimp", "doe", "gopher", "elephant", "giraffe", "spider", "puppy", "jay", "seal", "rooster", "turtle", "bull", "cat", "lamb", "rat", "slug", "buffalo", "blackbird", "swan", "lobster", "dog", "mosquito", "snake", "chicken", "anteater"]
d["a4a_sport"] = ["judo", "pool", "ride", "stretch", "helmet", "ice skating", "walk", "ran", "run", "swim", "hop", "hike", "boxing", "hockey", "race", "throw", "skate", "win", "squat", "ski", "golf", "whistle", "torch", "sailing", "stand", "tennis", "jump", "rowing", "jog", "rope"]
d["a4a_body"] = ["teeth", "cheek", "ankle", "knee", "toe", "muscle", "mouth", "feet", "hand", "elbow", "hair", "eyelash", "beard", "belly button", "thumb", "breast", "nostril", "nose", "hip", "arm", "eyebrow", "fist", "neck", "wrist", "throat", "eye", "leg", "spine", "ear", "finger", "foot", "braid", "face", "back", "chin", "bottom", "thigh", "belly"]
d["a4a_people"] = ["girl", "male", "son", "mates", "friends", "baby", "child", "dad", "mom", "twin boys", "brothers", "man", "mother", "grandfather", "family", "female", "wife", "husband", "bride", "madam", "grandmother", "couple", "lad", "twin girls", "tribe", "boy", "sisters", "woman", "lady"]
d["a4a_food"] = ["candy", "sausage", "hamburger", "steak", "fudge", "doughnut", "coconut", "rice", "ice cream", "jelly", "yoghurt", "dessert", "pretzel", "peanut", "jam", "feast", "cookie", "bacon", "spice", "coffee", "pie", "lemonade", "chocolate", "water bottle", "lunch", "ice", "sugar", "sauce", "soup", "juice", "fries", "cake", "mashed potatoes", "tea", "bun", "cheese", "beef", "sandwich", "slice", "sprinkle", "pizza", "flour", "gum", "spaghetti", "roast", "drink", "stew", "spread", "meat", "milk", "meal", "corn", "bread", "walnut", "egg", "hot dog", "ham"]
d["a4a_clothes_n_accessories"] = ["jewellery", "sock", "jacket", "heel", "smock", "shorts", "pocket", "necklace", "sweatshirt", "uniform", "raincoat", "trousers", "sunglasses", "coat", "pullover", "shirt", "sandals", "suit", "pyjamas", "skirt", "zip", "shoes", "jewel", "tie", "slippers", "gloves", "hat", "sleeve", "cap", "swimming suit", "trainer", "vest", "glasses", "shoelace", "patch", "scarf", "shoe", "button", "dress", "sash", "shoe sole", "robe", "pants", "kimono", "overalls"]
d["a4a_actions"] = ["lick", "slam", "beg", "fell", "scratch", "touch", "sniff", "see", "climb", "dig", "howl", "sleep", "explore", "draw", "hug", "teach", "nap", "clay", "catch", "clap", "cry", "sing", "meet", "sell", "peck", "beat", "kneel", "find", "dance", "cough", "cut", "think", "bark", "speak", "cheer", "bake", "write", "punch", "strum", "study", "plow", "dream", "post", "dive", "whisper", "sob", "shake", "feed", "crawl", "camp", "spill", "clean", "scream", "tear", "float", "pull", "ate", "kiss", "sit", "hatch", "blink", "hear", "smooch", "play", "wash", "chat", "drive", "drink", "fly", "juggle", "bit", "sweep", "look", "knit", "lift", "fetch", "read", "croak", "stare", "eat"]
d["a4a_construction"] = ["lighthouse", "door", "circus", "church", "kennel", "temple", "smoke", "chimney", "brick", "well", "street", "castle", "store", "staircase", "school", "farm", "bridge", "dam", "pyramid", "barn", "mill", "window", "cabin", "step", "shop", "shed", "roof", "steeple", "garage", "mosque", "hospital", "tent", "house", "wall", "bank", "shutter", "hut"]
d["a4a_nature"] = ["land", "cliff", "hill", "canyon", "rock", "sea", "lake", "coast", "shore", "mountain", "pond", "peak", "lava", "cave", "dune", "island", "forest", "desert", "iceberg"]
d["a4a_jobs"] = ["clown", "engineer", "priest", "vet", "judge", "chef", "athlete", "librarian", "juggler", "police", "plumber", "badge", "queen", "farmer", "magic", "knight", "doctor", "bricklayer", "cleaner", "teacher", "hunter", "soldier", "musician", "lawyer", "fisherman", "princess", "fireman", "nun", "chief", "pirate", "cowboy", "electrician", "nurse", "king", "president", "office", "carpenter", "jockey", "worker", "mechanic", "pilot", "actor", "cook", "student", "butcher", "accountant", "prince", "pope", "sailor", "boxer", "ballet", "coach", "astronaut", "painter", "anaesthesiologist", "scientist"]
d["a4a_fruit_n_veg"] = ["carrot", "blackberries", "celery", "turnip", "cacao", "peach", "melon", "grapefruit", "broccoli", "grapes", "spinach", "fig", "kernel", "radish", "tomato", "kiwi", "asparagus", "olives", "cucumbers", "beans", "strawberry", "peppers", "raspberry", "apricot", "potatoes", "peas", "cabbage", "cherries", "squash", "blueberries", "pear", "orange", "pumpkin", "avocado", "garlic", "onion", "apple", "lime", "cauliflower", "mango", "lettuce", "lemon", "aubergine", "artichokes", "plums", "leek", "bananas", "papaya"]
d["a4a_transport"] = ["sail", "taxi", "car", "bike", "raft", "pedal", "bus", "handlebar", "boat", "truck", "sleigh", "carpet", "motorcycle", "train", "ship", "van", "canoe", "rocket", "mast", "sledge", "bicycle"]
