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


numbers = ['Eins', 'Zwei', 'Drei', 'Vier', 'Fünf', 'Sechs', 'Sieben', 'Acht', 'Neun', 'Zehn', 'Elf', 'Zwölf' , 'Dreizehn', 'Vierzehn', 'Fünfzehn', 'Sechzehn', 'Siebzehn', 'Achtzehn', 'Neunzehn', 'Zwanzig', 'Einundzwanzig', 'Zweiundzwanzig', 'Dreiundzwanzig', 'Vierundzwanzig', 'Fünfundzwanzig', 'Sechsundzwanzig', 'Siebenundzwanzig', 'Achtundzwanzig', 'Neunundzwanzig']
numbers2090 = ['Zwanzig','Dreißig','Vierzig','Fünfzig','Sechzig','Siebzig','Achtzig','Neunzig']

nbrs = numbers[:]
nbrs[0] = "ein"
 
dp['abc_flashcards_word_sequence'] = ['Apfel', 'Hängematte', 'Blumen', 'Chinese', 'Ducken', 'Eule', 'Fisch',  'Giraffe', 'Haus','Iglu', 'Joghurt', 'Kaninchen', 'Löwe', 'Maus', 'Notizbuch', 'Ozean', 'Königin', 'Papagei', 'Qualle', 'Regenschirm','Sonne', 'Straße', 'Tomate', 'Umgehen', 'Schlüssel','Violine', 'Wassermelone', 'Xylophon', 'Yoga', 'Zebra']
d['abc_flashcards_word_sequence'] = ['<1>A<2>pfel', '<2>H<1>ä<2>ngematte', '<1>B<2>lumen', '<1>C<2>hinese ', '<1>D<2>ucken', '<1>E<2>ul<1>e', '<1>F<2>isch', '<1>G<2>iraffe', '<1>H<2>aus', '<1>I<2>glu', '<1>J<2>oghurt', '<1>K<2>aninchen', '<1>L<2>öwe', '<1>M<2>aus', '<1>N<2>otizbuch', '<1>O<2>zean', '<2>K<1>ö<2>nigin', '<1>P<2>apagei', '<1>Q<2>ualle ', '<1>R<2>egenschi<1>r<2>m', '<1>S<2>onne', '<2>Stra<1>ß<2>e', '<1>T<2>oma<1>t<2>e', '<1>U<2>mgehen', '<2>Schl<1>ü<2>ssel', '<1>V<2>ioline', '<1>W<2>assermelone', '<1>X<2>ylophon', '<1>Y<2>oga', '<1>Z<2>ebra']

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
    
    elif n == 0: return "Null"
    elif n == 100: return "Einhundert"
    return ""
    
    
def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'
    if m > 30:
        if h == 12: h = 1
        else: h += 1
    if m == 0: return "%s Uhr" % n2txt(h)
    elif m == 1: return "Eine Minute nach %s" % n2txt(h)
    elif m == 15: return "Viertel nach %s" % n2txt(h)
    elif m == 30:
        if h == 12:
            return "Halb %s" % n2txt(1)
        else:
            return "Halb %s" % n2txt(h+1)
    elif m == 45: return "Viertel vor %s" % n2txt(h)
    elif m == 59: return "Eine Minute vor %s" % n2txt(h)
    elif m < 30: return "%s nach %s" % (n2txt(m), n2txt(h))
    elif m > 30: return "%s vor %s" % (n2txt(60-m), n2txt(h))
    return ""
     
d["a4a_animals"] = ["Kuh", "Truthahn", "Schrimps", "Wolf", "Panther", "Panda", "Elster", "Muschel", "Pony", "Maus", "Mops", "Koala", "Frosch", "Marienkäfer", "Gorilla", "Lama", "Geier", "Hamster", "Vogel", "Seestern", "Krähe", "Sittich", "Raupe", "Tiger", "Kolibri", "Piranha", "Schwein", "Skorpion", "Fuchs", "Leopard", "Leguan", "Delfin", "Fledermaus", "Huhn", "Krabbe", "Henne", "Wespe", "Chameleon", "Wal", "Igel", "Rehkitz", "Elch", "Biene", "Viper", "Würger", "Esel", "Guinea Schwein", "Faultier", "Pferd", "Pinguin", "Otter", "Bär", "Zebra", "Strauß", "Kamel", "Antilope", "Lemur", "Taube", "Lama", "Maulwurf", "Rochen", "Widder", "Stinktier", "Qualle", "Schaf", "Hai", "Kätzchen", "Hirsch", "Schnecke", "Flamingo", "Hase", "Muschel", "Biber", "Spatz", "Taube", "Adler", "Käfer", "Nilpferd", "Eule", "Kobra", "Salamander", "Gans", "Kängeruh", "Libelle", "Kröte", "Pelikan", "Tintenfisch", "Löwenbaby", "Jaguar", "Ente", "Eidechse", "Rhinozeros", "Hyäne", "Ochse", "Pfau", "Papagei", "Elch", "Alligator", "Ameise", "Ziege", "Baby Hase", "Löwe", "Eichhörnchen", "Opossum", "Schimpanse", "Reh", "Erdhörnchen", "Elefant", "Giraffe", "Spinne", "Hundewelpe", "Tölpel", "Seelöwe", "Hahn", "Schildkröte", "Bulle", "Katze", "Lamm", "Ratte", "Schnecke", "Büffel", "Amsel", "Schwan", "Hummer", "Hund", "Moskito", "Schlange", "Hühnchen", "Ameisenbär"]
d["a4a_sport"] = ["Judo", "Billard", "Reiten", "Dehnen", "Helm", "Schlittschuh Laufen", "Gehen", "ran", "Laufen", "Schwimmen", "hop", "hike", "Boxen", "Hockey", "Rennen", "throw", "skate", "Gewinnen", "squat", "Skifahren", "Golf", "whistle", "torch", "sailing", "stand", "tennis", "jump", "rowing", "jog", "rope"]
d["a4a_body"] = ["Zähne", "cheek", "ankle", "Knie", "Zeh", "Muskel", "Mund", "Fuß", "Hand", "Ellbogen", "Haar", "eyelash", "Bart", "belly button", "thumb", "Brust", "nostril", "Nase", "Hüfte", "Arm", "Augenbraue", "Faust", "Nacken", "wrist", "throat", "eye", "Bein", "spine", "Ohr", "Finger", "Fuß", "braid", "Gesicht", "Rücken", "Kinn", "bottom", "thigh", "belly"]
d["a4a_people"] = ["Mädchen", "männlich", "Sohn", "Kumpel", "Freunde", "Baby", "Kind", "Vater", "Mutter", "Zwillinge", "Brüder", "Mann", "Mutter", "Großvater", "Familie", "weiblich", "Ehefrau", "Ehemann", "Braut", "Madame", "Großmutter", "Zusammen", "lad", "Zwillinge", "tribe", "Junge", "Schwestern", "Frau", "Lady"]
d["a4a_food"] = ["Süßigkeiten", "Wurst", "Hamburger", "Steak", "fudge", "Doughnut", "Kokosnuss", "Reis", "Eiscreme", "jelly", "Joghurt", "Nachtisch", "pretzel", "Erdnuss", "jam", "feast", "cookie", "bacon", "spice", "coffee", "pie", "lemonade", "chocolate", "water bottle", "lunch", "ice", "sugar", "sauce", "soup", "juice", "fries", "cake", "mashed potatoes", "tea", "bun", "cheese", "beef", "sandwich", "slice", "sprinkle", "pizza", "flour", "gum", "spaghetti", "roast", "drink", "stew", "spread", "meat", "milk", "meal", "corn", "bread", "walnut", "egg", "hot dog", "ham"]
d["a4a_clothes_n_accessories"] = ["Schmuck", "Socken", "Jacket", "heel", "smock", "Shorts", "Tasche", "necklace", "Sweatshirt", "Uniform", "Regenjacke", "Hose", "Sonnenbrille", "Jacke", "Pullover", "Shirt", "sandals", "Anzug", "pyjamas", "skirt", "zip", "shoes", "jewel", "tie", "slippers", "gloves", "hat", "sleeve", "cap", "swimming suit", "trainer", "vest", "glasses", "shoelace", "patch", "scarf", "shoe", "button", "dress", "sash", "shoe sole", "robe", "pants", "kimono", "overalls"]
d["a4a_actions"] = ["Lecken", "slam", "beg", "fell", "scratch", "Berühren", "sniff", "Sehen", "Klettern", "Graben", "howl", "Schlafen", "Erkunden", "Zeichnen", "Umarmen", "Lehren", "Ausruhen", "clay", "Fangen", "Klatschen", "Weinen", "Singen", "meet", "sell", "peck", "beat", "kneel", "find", "dance", "cough", "cut", "think", "bark", "speak", "cheer", "bake", "write", "punch", "strum", "study", "plow", "dream", "post", "dive", "whisper", "sob", "shake", "feed", "crawl", "camp", "spill", "clean", "scream", "tear", "float", "pull", "ate", "kiss", "sit", "hatch", "blink", "hear", "smooch", "play", "wash", "chat", "drive", "drink", "fly", "juggle", "bit", "sweep", "look", "knit", "lift", "fetch", "read", "croak", "stare", "eat"]
d["a4a_construction"] = ["Leuchtturm", "Tür", "Zirkus", "Kirche", "kennel", "Tempel", "Rauch", "Schornstein", "Ziegel", "well", "Straße", "Burg", "store", "Treppenhaus", "Schule", "Farm", "Brücke", "dam", "Pyramide", "barn", "mill", "window", "cabin", "step", "shop", "shed", "roof", "steeple", "garage", "mosque", "hospital", "tent", "house", "wall", "bank", "shutter", "hut"]
d["a4a_nature"] = ["Land", "Klippe", "Hügel", "Schlucht", "Felsen", "Meer", "See", "Küste", "shore", "Berg", "pond", "peak", "Lava", "Höhle", "Düne", "Insel", "Wald", "Wüste", "Eisberg"]
d["a4a_jobs"] = ["Clown", "Ingenieur", "Priester", "Veterinär", "Richter", "Koch", "Athlet", "Bibliothekar", "juggler", "Polizei", "Klempner", "badge", "Königin", "Farmer", "Magier", "Ritter", "Arzt", "Maurer", "Reiniger", "Lehrer", "hunter", "soldier", "musician", "lawyer", "fisherman", "princess", "fireman", "nun", "chief", "pirate", "cowboy", "electrician", "nurse", "king", "president", "office", "carpenter", "jockey", "worker", "mechanic", "pilot", "actor", "cook", "student", "butcher", "accountant", "prince", "pope", "sailor", "boxer", "ballet", "coach", "astronaut", "painter", "anaesthesiologist", "scientist"]
d["a4a_fruit_n_veg"] = ["Karotte", "blackberries", "celery", "turnip", "Kakao", "peach", "Melone", "Grapefruit", "Broccoli", "grapes", "spinach", "fig", "kernel", "radish", "Tomate", "Kiwi", "asparagus", "Oliven", "Gurken", "Bohnen", "strawberry", "peppers", "raspberry", "apricot", "potatoes", "peas", "cabbage", "cherries", "squash", "blueberries", "pear", "orange", "pumpkin", "avocado", "garlic", "onion", "apple", "lime", "cauliflower", "mango", "lettuce", "lemon", "aubergine", "artichokes", "plums", "leek", "bananas", "papaya"]
d["a4a_transport"] = ["sail", "Taxi", "Auto", "Rad", "raft", "Pedal", "Bus", "handlebar", "Boot", "Truck", "Schlitten", "carpet", "Motorrad", "Zug", "Schiff", "van", "Kanu", "Rakete", "Mast", "Schlitten", "Fahrrad"]
