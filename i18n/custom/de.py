# -*- coding: utf-8 -*-

#FAO Translators:
#First of all thank you for your interest in translating this game, 
#I will be grateful if you could share it with the community - 
#if possible please send it back to my email, and I'll add it to the next version.

#The translation does not have to be exact as long as it makes sense and fits in its location 
#(if it doesn't I'll try to either make the font smaller or make the area wider - where possible). 
#The colour names in other languages than English are already in smaller font.

#when translating the "d" dictionary please translate the values
#and leave keys as they are (the keys are sometimes shortened to save on space)

d = dict()
dp = dict() # messages with pronunciation exceptions - this dictionary will override entries in a copy of d


numbers = ['eins', 'zwei', 'drei', 'vier', 'fünf', 'sechs', 'sieben', 'acht', 'neun', 'zehn', 'elf', 'zwölf' , 'dreizehn', 'vierzehn', 'fünfzehn', 'sechzehn', 'siebzehn', 'achtzehn', 'neunzehn', 'zwanzig', 'einundzwanzig', 'zweiundzwanzig', 'dreiundzwanzig', 'vierundzwanzig', 'fünfundzwanzig', 'sechsundzwanzig', 'siebenundzwanzig', 'achtundzwanzig', 'neunundzwanzig']
numbers2090 = ['zwanzig','dreißig','vierzig','fünfzig','sechzig','siebzig','achtzig','neunzig']

nbrs = numbers[:]
nbrs[0] = "ein"
 
dp['abc_flashcards_word_sequence'] = ['Apfel', 'Hängematte', 'Blumen', 'C', 'Ducken', 'Eule', 'Fisch',  'Giraffe', 'Haus','Iglu', 'Joghurt', 'Kaninchen', 'Löwe', 'Maus', 'Notizbuch', 'Ozean', 'Königin', 'Papagei', 'Q', 'Regenschirm','Sonne', 'Straße', 'Tomate', 'Umgehen', 'Schlüssel','Violine', 'Wassermelone', 'Xylophon', 'Yoga', 'Zebra']
d['abc_flashcards_word_sequence'] = ['<1>A<2>pfel', '<2>H<1>ä<2>ngematte', '<1>B<2>lumen', '<1>C<2> ', '<1>D<2>ucken', '<1>E<2>ul<1>e', '<1>F<2>isch', '<1>G<2>iraffe', '<1>H<2>aus', '<1>I<2>glu', '<1>J<2>oghurt', '<1>K<2>aninchen', '<1>L<2>öwe', '<1>M<2>aus', '<1>N<2>otizbuch', '<1>O<2>zean', '<2>K<1>ö<2>nigin', '<1>P<2>apagei', '<1>Q<2> ', '<1>R<2>egenschi<1>r<2>m', '<1>S<2>onne', '<2>Stra<1>ß<2>e', '<1>T<2>oma<1>t<2>e', '<1>U<2>mgehen', '<2>Schl<1>ü<2>ssel', '<1>V<2>ioline', '<1>W<2>assermelone', '<1>X<2>ylophon', '<1>Y<2>oga', '<1>Z<2>ebra']

d['abc_flashcards_frame_sequence'] = [42, 56,36, 43,3,14,5,30,7,8, 73,17,11,12,13, 52,16,15, 43,20,18, 53,33,41,10,21,26,23,32,25]

#alphabet - de
alphabet_lc = ['a', 'ä', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p', 'q', 'r', 's', 'ß', 't', 'u', 'ü', 'v', 'w', 'x', 'y', 'z']
alphabet_uc = ['A', 'Ä', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'Ö', 'P', 'Q', 'R', 'S', 'ß', 'T', 'U', 'Ü', 'V', 'W', 'X', 'Y', 'Z']
#correction of eSpeak pronounciation of single letters if needed
letter_names = []
accents_lc = ['-']
accents_uc = []

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
            ones = nbrs[m-1]
            if twoliner:
                return [ones + "und-", tens]
            else:
                return ones + "und" + tens
    
    elif n == 0: return "null"
    elif n == 100: return "einhundert"
    return ""
    
    
def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if m == 0: return "%s o'clock" % n2txt(h)
    elif m == 1: return "one minute past %s" % n2txt(h)
    elif m == 15: return "quarter past %s" % n2txt(h)
    elif m == 30: return "half past %s" % n2txt(h)
    elif m == 45: return "quarter to %s" % n2txt(h)
    elif m == 59: return "one minute to %s" % n2txt(h)
    elif m < 30: return "%s past %s" % (n2txt(m), n2txt(h))
    elif m > 30: return "%s to %s" % (n2txt(60-m), n2txt(h))
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
