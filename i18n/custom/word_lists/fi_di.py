# -*- coding: utf-8 -*-

#this is a list of words used by the word builder and word maze games and possibly
#other games built in the future
#these words are a naive translation of a part of most commonly used words in English
#in each sub-list in the list di first number is a number of words in the sublist
#to aviod counting it every time the list is selected
#the sublists are consisting of words with len() of 3 - 10
#I think the way of going about internationalization here would be to create a new list
#with words most commonly used in your language rather than translating the English version

di = [[84, 'aja', 'ala', 'ano', 'apu', 'aro', 'ase', 'asu', 'eli', 'elo', 'elä', 'emo', 'eri', 'ero', 'etu', 'hän', 'ies', 'iho', 'ikä', 'ilo', 'iso', 'isä', 'itä', 'joi', 'jos', 'juo', 'jäi', 'jää', 'kai', 'koe', 'koi', 'kun', 'kuu', 'kyy', 'käy', 'loi', 'lue', 'luo', 'luu', 'lyö', 'löi', 'maa', 'myi', 'myy', 'nuo', 'nyt', 'näe', 'näy', 'ohi', 'oli', 'olo', 'oma', 'opi', 'osa', 'ota', 'ovi', 'pii', 'pue', 'puu', 'pää', 'saa', 'sai', 'sen', 'soi', 'suo', 'suu', 'syy', 'syö', 'söi', 'tai', 'tee', 'tie', 'tuo', 'työ', 'uni', 'vai', 'vei', 'vie', 'voi', 'vyö', 'yhä', 'yli', 'yöt', 'äly', 'älä'],
[397, 'aamu', 'aasi', 'aava', 'aave', 'ahjo', 'ahne', 'aihe', 'aika', 'aina', 'aion', 'aita', 'ajat', 'alan', 'alas', 'alat', 'alin', 'alku', 'alla', 'alle', 'alta', 'alue', 'anna', 'anoa', 'ansa', 'appi', 'apua', 'aran', 'arka', 'armo', 'arpa', 'arpi', 'arvo', 'asia', 'asti', 'astu', 'asua', 'asui', 'asun', 'asuu', 'auki', 'auta', 'auto', 'avaa', 'edes', 'ehdi', 'eheä', 'ehkä', 'ehyt', 'eikä', 'eikö', 'eipä', 'eksy', 'elin', 'elon', 'elän', 'elät', 'emme', 'enkö', 'entä', 'enää', 'eroa', 'eräs', 'esti', 'estä', 'etkä', 'etkö', 'etsi', 'ette', 'että', 'eviä', 'evät', 'haju', 'haki', 'halu', 'hela', 'heti', 'hioa', 'huhu', 'huku', 'hyvä', 'hätä', 'häät', 'idän', 'ihme', 'ihoa', 'ihra', 'ilma', 'ilme', 'ilmi', 'iloa', 'ilon', 'ilta', 'imeä', 'into', 'irti', 'iske', 'iski', 'isku', 'istu', 'isän', 'isät', 'isää', 'itki', 'itku', 'itse', 'itää', 'iäti', 'jako', 'jalo', 'jano', 'joen', 'joet', 'joka', 'joki', 'joko', 'joku', 'jopa', 'jota', 'juna', 'juon', 'juot', 'jyvä', 'jäin', 'jäit', 'jätä', 'jään', 'kala', 'kana', 'kato', 'katu', 'kehä', 'kesy', 'kesä', 'keto', 'ketä', 'kipu', 'kita', 'kivi', 'koki', 'koko', 'kone',  'kori', 'kova', 'kuin', 'kuka', 'kuri', 'kuun', 'kuva', 'kyky', 'kylä', 'kynä', 'kysy', 'käly', 'käsi', 'kävi', 'käyn', 'lait', 'laki', 'lama', 'lapa', 'lasi', 'lepo', 'levy', 'liha', 'liki', 'loit', 'loka', 'luen', 'luit', 'luja', 'luki', 'luku', 'lumi', 'lupa', 'luut', 'lyön', 'lyöt', 'läpi', 'löit', 'maan', 'maat', 'maha', 'maja', 'maku', 'mato', 'mehu', 'melu', 'mene', 'meni', 'meno', 'meri', 'mesi', 'mies', 'mikä', 'minä', 'mitä', 'moni', 'muka', 'muut', 'myyt', 'myös', 'mätä', 'nenä', 'niin', 'nimi', 'noin', 'nuku', 'näen', 'näet', 'näin', 'näki', 'näky', 'näkö', 'nämä', 'näyn', 'näön', 'ohra', 'ohut', 'oksa', 'olen', 'olet', 'olin', 'olit', 'olki', 'olla', 'oman', 'omat', 'onki', 'onko', 'onni', 'oppi', 'orhi', 'orja', 'orpo', 'orsi', 'osaa', 'osta', 'osti', 'osua', 'otan', 'otin', 'otsa', 'otti', 'outo', 'ovat', 'oven', 'ovet', 'ovia', 'paha', 'pala', 'palo', 'pari', 'pata', 'peri', 'perä', 'pese', 'pesi', 'peto', 'pian', 'pidä', 'piha', 'piti', 'pito', 'pois', 'puhe', 'puku', 'puro', 'puun', 'puut', 'pyhä', 'päät', 'pöly', 'raha', 'raja', 'raju', 'rapa', 'runo', 'sade', 'saha', 'sali', 'sama', 'sana', 'sano', 'sata', 'sato', 'satu', 'savi', 'savu', 'seis', 'sekä', 'sekö', 'setä', 'side', 'sido', 'siis', 'sija', 'sika', 'sinä', 'siru', 'sisu', 'sitä', 'sivu', 'sora', 'sota', 'soti', 'suku', 'sula', 'suli', 'sumu', 'suot', 'suru', 'susi', 'sysi', 'syvä', 'syön', 'söin', 'söit', 'taas', 'talo', 'teki', 'teko', 'tekö', 'teon', 'teot', 'tepä', 'terä', 'tiet', 'tila', 'tili', 'tina', 'toit', 'toki', 'tomu', 'tora', 'tosi', 'tuet', 'tuho', 'tuki', 'tule', 'tuli', 'tulo', 'tuon', 'tykö', 'tyly', 'työn', 'työt', 'tämä', 'tänä', 'tätä', 'uhma', 'uhri', 'ulos', 'unet', 'unia', 'unta', 'urat', 'urho', 'usko', 'uuni', 'uusi', 'vaan', 'vaha', 'vain', 'vala', 'valo', 'vara', 'varo', 'vati', 'vedä', 'vein', 'veli', 'veri', 'vero', 'vesi', 'veti', 'viha', 'vika', 'vilu', 'voit', 'vyön', 'vyöt', 'väki', 'väsy', 'vävy', 'yhtä', 'yksi', 'ylen', 'ylin', 'ylle', 'yllä', 'yltä', 'ylös', 'ynnä', 'yötä', 'äiti', 'ääni', 'öljy'],
[609, 'aamun', 'aarre', 'aasia', 'aasin', 'aasit', 'aavat', 'ahdas', 'ahnas', 'aidan', 'aikoi', 'aikoo', 'ainoa', 'aitat', 'aivan', 'aivot', 'alati', 'alkaa', 'alkua', 'allas', 'almut', 'aloit', 'altis', 'annos', 'anova', 'ansat', 'ansio', 'antoi', 'apuna', 'arjen', 'arkin', 'arkki', 'arkku', 'arkun', 'armas', 'arvan', 'arvet', 'arvon', 'aseet', 'asema', 'aseta', 'asiat', 'askel', 'astia', 'astua', 'asuja', 'aukko', 'aukot', 'autio', 'avain', 'avara', 'avata', 'avoin', 'ehdot', 'eheät', 'eilen', 'eksyä', 'eläin', 'elämä', 'elävä', 'ennen', 'ensin', 'erota', 'eräät', 'esine', 'etana', 'etsin', 'etsiä', 'eväät', 'farao', 'haamu', 'haava', 'hahmo', 'hajut', 'hakea', 'halko', 'halpa', 'hanke', 'hanki', 'harja', 'hauta', 'hehku', 'heimo', 'heinä', 'helle', 'henki', 'herra', 'hetki', 'hidas', 'hieno', 'hiiri', 'hinta', 'hirmu', 'hirsi', 'hohde', 'hohto', 'hopea', 'huilu', 'hullu', 'huoli', 'huone', 'huono', 'huopa', 'hurja', 'huuto', 'hylky', 'hyöty', 'häijy', 'häkki', 'häntä', 'häpeä', 'härkä', 'häviö', 'ihana', 'ikinä', 'ikävä', 'ilkeä', 'illan', 'iskeä', 'iskut', 'istua', 'itkeä', 'iäkäs', 'jalka', 'jolla', 'jolle', 'jolta', 'jonka', 'jonne', 'jossa', 'josta', 'joten', 'jotka', 'jotta', 'jousi', 'juhla', 'juhta', 'julma', 'juoda', 'juoma', 'juoni', 'juuri', 'jyvät', 'järvi', 'jäsen', 'jäädä', 'kaari', 'kahle', 'kaide', 'kaihi', 'kaita', 'kaivo', 'kakku', 'kaksi', 'kalat', 'kammo', 'kanne', 'kansa', 'kanto', 'kapea', 'karhu', 'karja', 'karmi', 'kasat', 'kaste', 'katku', 'katso', 'katua', 'kauan', 'kauas', 'kauhu', 'kaula', 'kehua', 'kehät', 'kelpo', 'kenkä', 'kerta', 'ketkä', 'ketut', 'keveä', 'kevyt', 'kidat', 'kieli', 'kiero', 'kilpi', 'kipeä', 'kirja', 'kirje', 'kisko', 'kivet', 'kohta', 'kohti', 'kohtu', 'koira', 'kokea', 'kolme', 'komea', 'konna', 'koota', 'kopea', 'korsi', 'korva', 'koska', 'koski', 'kosto', 'kotka', 'kuiva', 'kukka', 'kukko', 'kulku', 'kulta', 'kuohu', 'kuori', 'kuppi', 'kurja', 'kurki', 'kutsu', 'kuulo', 'kuuma', 'kuume', 'kuuro', 'kuusi', 'kylki', 'kyllä', 'kylmä', 'kylvö', 'kyntö', 'kypsä', 'kysyä', 'kädet', 'kärki', 'käsky', 'kätkö', 'käydä', 'köyhä', 'laaja', 'lahja', 'lahko', 'laita', 'laite', 'laiva', 'lakko', 'lanka', 'lanta', 'lapio', 'lapsi', 'lasku', 'lasta', 'latva', 'laulu', 'lauma', 'lause', 'lauta', 'lavea', 'lehmä', 'lehti', 'lehvä', 'leili', 'leipä', 'leiri', 'leski', 'leveä', 'liemi', 'liesi', 'lihat', 'liike', 'liina', 'linna', 'lintu', 'lippu', 'lista', 'loppu', 'lukea', 'luoda', 'luoja', 'luola', 'luumu', 'luuta', 'lyhde', 'lyhyt', 'lyijy', 'lyödä', 'lyöjä', 'lähes', 'lähin', 'lähtö', 'läksy', 'läsnä', 'lääke', 'löydä', 'madot', 'mahat', 'mahla', 'maine', 'maito', 'makea', 'maksa', 'malja', 'malli', 'malmi', 'manna', 'marja', 'massa', 'matka', 'matto', 'mehua', 'mennä', 'metsä', 'mieli', 'mihin', 'miina', 'miksi', 'millä', 'miltä', 'miniä', 'minkä', 'minne', 'missä', 'mistä', 'miten', 'mitkä', 'mitta', 'monta', 'multa', 'muona', 'muoto', 'murhe', 'musta', 'mutta', 'muuli', 'muuri', 'mykkä', 'myydä', 'myyjä', 'myyrä', 'määrä', 'nahka', 'nauha', 'nauru', 'nauta', 'neito', 'neliö', 'neljä', 'neste', 'neuvo', 'nielu', 'niska', 'noita', 'nokka', 'nopea', 'nuhde', 'nuija', 'nuoli', 'nuora', 'nuppu', 'nurja', 'nähdä', 'näkyä', 'nälkä', 'näytä', 'nöyrä',  'oikea', 'oinas', 'omena', 'onkia', 'ontto', 'ontua', 'oppia', 'osuus', 'ottaa', 'ovela', 'paeta', 'paino', 'paise', 'pakko', 'paksu', 'palmu', 'pappi', 'paras', 'parku', 'parta', 'parvi', 'pauhu', 'pauke', 'peite', 'pelko', 'pelto', 'perhe', 'periä', 'pesiä', 'pestä', 'pesue', 'petos', 'peura', 'pieni', 'pihvi', 'pilvi', 'pimeä', 'pinta', 'piste', 'pitkä', 'pohja', 'poika', 'polku', 'polte', 'polvi', 'puhua', 'pukea', 'puoli', 'puuha', 'puute', 'pysyä', 'päivä', 'pätsi', 'pöytä', 'raaka', 'raato', 'rakas', 'rampa', 'ranta', 'rasva', 'ratsu', 'rauha', 'rauta', 'reikä', 'reisi', 'retki', 'reuna', 'riemu', 'riita', 'rikas', 'rikki', 'rikos', 'risti', 'rosvo', 'rouva', 'ruhje', 'runko', 'ruoho', 'ruoka', 'ruoko', 'rutto', 'ryhmä', 'ryske', 'sanoa', 'sarvi', 'sauva', 'seimi', 'seinä', 'selvä', 'seppä', 'seura', 'seutu', 'sielu', 'siipi', 'siksi', 'sillä', 'silmä', 'silti', 'sinne', 'sisar', 'sisko', 'sisus', 'siten', 'sitoa', 'soida', 'sokea', 'sopia', 'sormi', 'sorto', 'sotia', 'sulat', 'sulje', 'suoja', 'suola', 'suora', 'suuri', 'sydän', 'sylki', 'synti', 'syödä', 'sähkö', 'säkki', 'sänky', 'särki', 'sävel', 'sääli', 'tahra', 'tahto', 'taimi', 'taito', 'takki', 'takoa', 'talvi', 'tarha', 'tasan', 'taulu', 'tauti', 'teema', 'tehdä', 'tehty', 'terve', 'testi', 'tieto', 'tiili', 'tiuku', 'toimi', 'toivo', 'torit', 'torni', 'totta', 'tuhat', 'tuhka', 'tuima', 'tukea', 'tukka', 'tukki', 'tulli', 'tulos', 'tulva', 'tunne', 'tunto', 'tuoda', 'tuoja', 'tuoli', 'tuore', 'turha', 'turta', 'turva', 'tuska', 'tuuli', 'tyhjä', 'tyhmä', 'tyttö', 'tytär', 'tyven', 'tyyni', 'tähkä', 'tähti', 'tänne', 'tässä', 'täysi', 'uhkea', 'uljas', 'vaaka', 'vaara', 'vaari', 'vaate', 'vahva', 'vaimo', 'vaino', 'vaiva', 'vakaa', 'valaa', 'valhe', 'valio', 'valli', 'valta', 'vamma', 'vanha', 'vanki', 'vapaa', 'varas', 'varjo', 'varma', 'varsa', 'varsi', 'vasen', 'vaski', 'vasta', 'vatsa', 'vehnä', 'veisu', 'velka', 'verho', 'verso', 'vielä', 'viini', 'viiri', 'viisi', 'viiva', 'vilja', 'villa', 'virka', 'virsi', 'virta', 'vitsa', 'voide', 'voima', 'vuode', 'vuohi', 'vuori', 'vuoro', 'vuosi', 'vuoto', 'vähän', 'väsyä', 'väärä', 'väärä', 'yksin', 'ylevä', 'ylpeä', 'yltyä', 'ylväs', 'yrtti', 'yöpyä', 'äidit', 'äsken', 'öinen', 'öljyt'],
[494,'ahneus', 'aikana', 'aiottu', 'aitaus', 'ajaton', 'ajatus', 'alasti', 'alussa', 'alusta', 'ammoin', 'ankara', 'anoppi', 'asukas', 'asumus', 'asunto', 'ateria', 'edeltä', 'edessä', 'edestä', 'emäntä', 'enkeli', 'etikka', 'etsivä', 'grilli', 'hakata', 'hamara', 'hammas', 'harmaa', 'harppu', 'harras', 'hautoa', 'hehkua', 'heidät', 'heikko', 'helppo', 'hiekka', 'hiljaa', 'hirnua', 'hohtaa', 'hoitaa', 'horjua', 'huippu', 'humaus', 'hunaja', 'huojua', 'huomio', 'hypätä', 'hyvyys', 'häilyä', 'hyminä', 'häipyä', 'hävetä', 'ikenet', 'ikkuna', 'istuin', 'isäntä', 'jaettu', 'jatkaa', 'joihin', 'jonkun', 'joskus', 'jotain', 'joukko', 'juhlat', 'julkea', 'juoksu', 'jylinä', 'jyrinä', 'jyrkkä', 'jytinä', 'jättää', 'kaappi', 'kaarna', 'kaataa', 'kaatua', 'kaavio', 'kadota', 'kahdes', 'kahina', 'kaiken', 'kaikki', 'kaisla', 'kaivos', 'kajota', 'kalkki', 'kallis', 'kamana', 'kammio', 'kangas', 'kankea', 'kannel', 'kanssa', 'kantaa', 'kapina', 'kapine', 'karate', 'karhea', 'karjua', 'karsia', 'karvas', 'kastaa', 'kasvaa', 'kasvot', 'kateus', 'katkoa', 'katsoa', 'katuva', 'kauhea', 'kaunis', 'kautta', 'keihäs', 'keitto', 'keksiä', 'kekäle', 'kenttä', 'kerran', 'kerros', 'kertoa', 'keskus', 'ketään', 'kiehua', 'kielto', 'kieriä', 'kietoa', 'kiilto', 'kiinni', 'kiista', 'kiitos', 'kiitää', 'kiivas', 'kiljua', 'kirkas', 'kirota', 'kirous', 'kirves', 'kitara', 'kiukku', 'koetus', 'kohden', 'kohota', 'koiras', 'koitos', 'koitto', 'koitua', 'kokous', 'kolina', 'kolmas', 'kolmen', 'komeus', 'kookas', 'kopeus', 'koreus', 'korkea', 'koroke', 'koskea', 'kostua', 'kruunu', 'kuinka', 'kukaan', 'kukkia', 'kumina', 'kunkin', 'kunnes', 'kunnia', 'kuohua', 'kuoppa', 'kuoria', 'kuorma', 'kutsua', 'kuuden', 'kuudes', 'kuulla', 'kuulua', 'kynnys', 'kypsyä', 'kypärä', 'kytkeä', 'kytkin', 'kärkäs', 'kärsiä', 'käskeä', 'kätkeä', 'käärme', 'laakso', 'laasti', 'lahjus', 'laidun', 'laiska', 'laiton', 'lakata', 'lammas', 'lamppu', 'lantio', 'laskea', 'laskin', 'lattia', 'laulaa', 'lausua', 'lempeä', 'lentää', 'leppyä', 'leveys', 'levitä', 'liekki', 'lihava', 'liitto', 'liitää', 'liukas', 'loinen', 'loiste', 'loisto', 'lonkka', 'louhia', 'lukija', 'lumous', 'luokse', 'luomus', 'luotto', 'lupaus', 'lymytä', 'lyöjät', 'löyhkä', 'löytää', 'maissi', 'makeus', 'manala', 'manata', 'marssi', 'matala', 'mehevä', 'merkki', 'meteli', 'miekka', 'mikäli', 'mikään', 'mitään', 'muhkea', 'muisti', 'muisto', 'mukana', 'murtaa', 'muutos', 'myrkky', 'myrsky', 'myöten', 'märkiä', 'naaras', 'nainen', 'neljäs', 'neuvoa', 'niellä', 'niinkö', 'niinpä', 'nousta', 'nukkua', 'numero', 'nylkeä', 'nyrkki', 'näkevä', 'näkyvä', 'odotus', 'ohdake', 'oikein', 'oikeus', 'olemus', 'olento', 'olijat', 'opetus', 'osasto', 'paarit', 'paarma', 'paasto', 'pahuus', 'paikka', 'paimen', 'painaa', 'painua', 'paitsi', 'palata', 'paljas', 'paljon', 'palkka', 'pantti', 'parkua', 'pasuna', 'patsas', 'peikko', 'peitsi', 'peitto', 'pelkkä', 'pensas', 'penseä', 'pettyä', 'piirto', 'pilata', 'pilkka', 'pilkku', 'pimeys', 'pisara', 'pituus', 'poikki', 'poimia', 'poissa', 'poljin', 'polkea', 'portti', 'potkia', 'pudota', 'puhdas', 'puhuja', 'pusero', 'pyhyys', 'pylväs', 'pyrstö', 'pyydys', 'pyyntö', 'pyöreä', 'pyöriä', 'pätevä', 'päälle', 'päällä', 'rahvas', 'raikas', 'raitis', 'raskas', 'ravita', 'rehevä', 'rengas', 'riehua', 'riista', 'rikkoa', 'rohkea', 'ruhjoa', 'rukous', 'runsas', 'ruoska', 'ruoste', 'ruskea', 'ruukku', 'ruumis', 'ryhtyä', 'ryöstö', 'rätinä', 'saakka', 'saalis', 'sairas', 'salama', 'salata', 'sallia', 'sammua', 'samoin', 'sangen', 'sankka', 'sanoma', 'satama', 'satula', 'seinät', 'serkku', 'seuloa', 'siellä', 'siemen', 'siivet', 'sirppi', 'sitten', 'soitto', 'sokeri', 'sopiva', 'sormus', 'sortua', 'sotiva', 'soturi', 'suojus', 'suosio', 'sureva', 'surkea', 'suulas', 'suunta', 'synkeä', 'synkkä', 'syvyys', 'syytön', 'syösty', 'säilyä', 'särkeä', 'särkyä', 'särpiä', 'säädin', 'säädös', 'sääntö', 'säästä', 'säästö', 'taakka', 'taipua', 'taivas', 'takana', 'tanssi', 'tapaus', 'tappio', 'tarkka', 'tasaus', 'tavara', 'tavata', 'tekijä', 'teline', 'teltta', 'terävä', 'tilava', 'tippua', 'tiukka', 'toimia', 'toinen', 'toisen', 'toisin', 'toista', 'totuus', 'toukka', 'toveri', 'tukkia', 'tuleva', 'tulvia', 'tunkio', 'tuntea', 'tuoksu', 'tuolla', 'tuolta', 'tuomio', 'tuonne', 'tuossa', 'tuskin', 'tutkia', 'tänään', 'tärkeä', 'täynnä', 'täysin', 'täällä', 'täältä', 'töminä', 'uneton', 'upotus', 'useita', 'vaahto', 'vaikea', 'vaikka', 'vainio', 'vakuus', 'valkea', 'valmis', 'valvoa', 'vanhus', 'vannoa', 'vapaus', 'varten', 'vasara', 'vaunut', 'vedota', 'veitsi', 'veltto', 'verkko', 'verran', 'versoa', 'viekas', 'vietto', 'vihata', 'vihmoa', 'vihreä', 'viiden', 'viides', 'viikko', 'viisas', 'viitta', 'viittä', 'vilppi', 'viruva', 'voitto', 'vuokra', 'vuoksi', 'vuoret', 'vyöryä', 'väestö', 'vähyys', 'väijyä', 'väkevä', 'yhteen', 'yhteys', 'ylitse', 'ylpeys', 'ympyrä', 'ympäri', 'ystävä', 'äkisti', 'älytön', 'ärjyvä', 'ääneti', 'ääreen'],
[439,'aavikko', 'ahertaa', 'aikomus', 'ainakin', 'akaatti', 'alainen', 'alaston', 'alentua', 'alistua', 'alttari', 'ammatti', 'anastaa', 'ankkuri', 'annettu', 'antoisa', 'armoton', 'arvoton', 'asettua', 'aurinko', 'auttaja', 'avartaa', 'avautua', 'avoinna', 'avustaa', 'avustus', 'eilinen', 'eläköön', 'enemmän', 'energia', 'entinen', 'eteinen', 'gaselli', 'haastaa', 'haihtua', 'haikara', 'haljeta', 'hallava', 'hallita', 'haltija', 'halukas', 'hangata', 'hankkia', 'harkita', 'harvoin', 'haudata', 'haukkua', 'havaita', 'hedelmä', 'hehkuva', 'hellyys', 'henkäys', 'herjata', 'hevonen', 'hoitaja', 'horjuva', 'hulluus', 'huokaus', 'huomata', 'hyljätä', 'hyvitys', 'hyökätä', 'häijyys', 'häiritä', 'hälytys', 'hävitys', 'ihanuus', 'ihastua', 'ihastus', 'ihminen', 'ikuinen', 'iloinen', 'ilostua', 'ilveily', 'istukas', 'istutus', 'itsensä', 'jalusta', 'johtaja', 'jotakin', 'joukkio', 'julkeus', 'juotava', 'juttelu', 'juurtua', 'jälkeen', 'jälleen', 'järkkyä', 'jäännös', 'kaiketi', 'kaivata', 'kalista', 'kaljuus', 'kalmari', 'kalusto', 'kankuri', 'kantele', 'kappale', 'karitsa', 'karsina', 'karttua', 'katkera', 'katketa', 'kaukana', 'kauneus', 'kaupata', 'keisari', 'kelvata', 'keneksi', 'kenelle', 'kenellä', 'kenties', 'kerskua', 'kertoja', 'kestävä', 'kiertyä', 'kiittää', 'kiljuva', 'kirjain', 'kirjava', 'kirjuri', 'kirottu', 'kiskuri', 'kiusaus', 'koettaa', 'kohdata', 'kohoava', 'kohtalo', 'kohtuus', 'koittaa', 'kokeilu', 'kokemus', 'kolmena', 'korjaus', 'korkeus', 'korvata', 'koskaan', 'kostaja', 'kudottu', 'kuihtua', 'kuivuus', 'kukkaro', 'kukkula', 'kulkija', 'kulunut', 'kuohuva', 'kuolema', 'kuoleva', 'kuollut', 'kuulija', 'kuumuus', 'kyntäjä', 'kysymys', 'kyynärä', 'käskijä', 'kävellä', 'käyttää', 'käytävä', 'kääntyä', 'kääntää', 'köyhyys', 'köynnös', 'köyttää', 'laihtua', 'laittaa', 'lauhtua', 'laupeus', 'leijona', 'leikata', 'leikkiä', 'leimaus', 'leipuri', 'lentävä', 'levoton', 'lietsoa', 'liittyä', 'liitävä', 'loistaa', 'lopuksi', 'lopulla', 'lopulta', 'lujasti', 'lumottu', 'luonnos', 'luottaa', 'läheltä', 'lähetys', 'lähtevä', 'lätäkkö', 'löytävä', 'maailma', 'mahtava', 'mainita', 'matkata', 'melkein', 'merkitä', 'mestari', 'metalli', 'miettiä', 'mikähän', 'milloin', 'minkään', 'mitätön', 'monesti', 'morsian', 'muinoin', 'muistaa', 'muutoin', 'muuttaa', 'muuttua', 'myöntyä', 'myöntää', 'määrätä', 'määräys', 'naapuri', 'nahkuri', 'nauttia', 'niittää', 'niskuri', 'noituus', 'nouseva', 'nuortua', 'nuoruus', 'nystyrä', 'nääntyä', 'nöyrtyä', 'nöyryys', 'odottaa', 'ohjelma', 'omistaa', 'ongelma', 'onnekas', 'onneton', 'opastaa', 'opettaa', 'oppinut', 'orjatar', 'pahempi', 'paikoin', 'painava', 'paksuus', 'palanen', 'paljous', 'pantata', 'papisto', 'parasta', 'parempi', 'parhain', 'peittyä', 'peittää', 'perintö', 'petturi', 'pidellä', 'pienuus', 'piirtää', 'pilkata', 'pistävä', 'pitäisi', 'poistaa', 'poistua', 'polkija', 'polttaa', 'portaat', 'potkuri', 'prinssi', 'puhjeta', 'puhkeaa', 'puhuttu', 'punnita', 'puntari', 'puoleen', 'puoliso', 'puuttua', 'päivänä', 'päähine', 'päättyä', 'päättää', 'pöyhkeä', 'raastaa', 'raivata', 'rakkaus', 'rasitus', 'ravitse', 'rientää', 'riippua', 'riistää', 'rikkaus', 'rikottu', 'riuhtoa', 'rohkeus', 'rubiini', 'runsaus', 'rupinen', 'rynnätä', 'ryöstää', 'ryöväri', 'röyhelö', 'röyhkeä', 'saapuva', 'saartaa', 'saastua', 'safiiri', 'saippua', 'sairaus', 'salattu', 'samalla', 'sankari', 'selitys', 'selusta', 'seppele', 'seurata', 'siepata', 'siirtyä', 'siirtää', 'silloin', 'sinetti', 'sisälle', 'siunaus', 'sivusto', 'sopimus', 'sorkkia', 'sortaja', 'sortuva', 'sotilas', 'sovinto', 'sovitus', 'suistua', 'suitset', 'sukkula', 'suojata', 'suoruus', 'suostua', 'suuruus', 'suuttua', 'synkeys', 'syöksyä', 'säteily', 'sävyisä', 'säästyä', 'säästää', 'tahansa', 'tahkota', 'tahrata', 'taikina', 'taitava', 'taittaa', 'tappaja', 'tarjota', 'tarttua', 'tasanko', 'tehoton', 'tehtävä', 'tietäjä', 'tiputus', 'todella', 'todiste', 'tohveli', 'toisena', 'topaasi', 'toraisa', 'totella', 'tuhottu', 'tulinen', 'tuoksua', 'tuomari', 'tuonela', 'tuottaa', 'turhuus', 'turisti', 'turvata', 'tutkija', 'tuttava', 'tyhjyys', 'tyhmyys', 'tyyntyä', 'työntää', 'täyttyä', 'täyttää', 'törmätä', 'ukkonen', 'ulottua', 'uutiset', 'vaativa', 'vaellus', 'vahvuus', 'vainaja', 'vainuta', 'vakooja', 'valinta', 'valittu', 'valitus', 'valkeus', 'valoisa', 'valtias', 'vanheta', 'vapista', 'varakas', 'varhain', 'varista', 'varjoaa', 'varmuus', 'vartalo', 'vartija', 'varttua', 'vasikka', 'vastaan', 'vastata', 'vastaus', 'veisata', 'verrata', 'viereen', 'viettää', 'vihdoin', 'viihtyä', 'viileys', 'viimein', 'viisaus', 'viittoa', 'virkkoa', 'viskata', 'visusti', 'vitsaus', 'vuotava', 'vyöttää', 'väittää', 'välillä', 'välissä', 'vääntyä', 'vääntää', 'vääryys', 'yhdessä', 'yhdiste', 'yleensä', 'yleinen', 'ylistys', 'yrittää', 'ärjyntä', 'ärjäisy', 'äänetön', 'ääressä'],
[235, 'ahdistus', 'ahkeruus', 'aivastus', 'aivoitus', 'antautua', 'anteeksi', 'antelias', 'armahtaa', 'armelias', 'arvioida', 'arvoitus', 'edelleen', 'ennustaa', 'ennustus', 'erillään', 'haarukka', 'hallitus', 'heikkous', 'heilutus', 'herättää', 'hetkinen', 'hietikko', 'hillitty', 'hitaasti', 'houkutus', 'hukuttaa', 'hullutus', 'huomenna', 'huominen', 'huuhkaja', 'hymähtää', 'hyökkäys', 'hämminki', 'hämärtää', 'hävittää', 'ilmestys', 'ilmestyä', 'ilmoitus', 'irtautua', 'johdatus', 'johdotus', 'jokainen', 'julistaa', 'julistus', 'julkinen', 'kadottaa', 'kannikka', 'kansleri', 'kastella', 'kataluus', 'katsella', 'kauppias', 'kaupunki', 'kavaltaa', 'kavaluus', 'keittäjä', 'kerskata', 'kihlattu', 'kiiltävä', 'kiljunta', 'kiristys', 'kirkkaus', 'kiusaaja', 'kiusattu', 'kokonaan', 'korostaa', 'korottaa', 'korskeus', 'kovettua', 'kriketti', 'kuiskaus', 'kukkanen', 'kumartua', 'kummitus', 'kumppani', 'kuningas', 'kunnolla', 'kuorsata', 'kurittaa', 'kuukausi', 'kuuluisa', 'kuvastin', 'kymmenes', 'kärpänen', 'kärsimys', 'laiskuus', 'lakastua', 'lammikko', 'lauselma', 'lausunto', 'levittää', 'lihavuus', 'lintunen', 'lohdutus', 'loistava', 'luhistua', 'lunastaa', 'lunastus', 'lähettää', 'lääkitys', 'mahdoton', 'mansikka', 'masentua', 'menestys', 'menestyä', 'menettää', 'merkitty', 'merkitys', 'miehekäs', 'mieletön', 'molemmat', 'murhaaja', 'mustelma', 'muuttuva', 'märehtiä', 'neitonen', 'neulanen', 'neuvosto', 'nopeasti', 'omaisuus', 'onnistua', 'opettaja', 'osoittaa', 'paastota', 'pahennus', 'pakkanen', 'pakottaa', 'palmikko', 'palvella', 'palvelus', 'panssari', 'pantteri', 'parannus', 'pelastaa', 'peljätys', 'pelottaa', 'permanto', 'perustus', 'pettymys', 'piiritys', 'pimentää', 'poikanen', 'pudistaa', 'puhallus', 'puhaltaa', 'punainen', 'puolikas', 'puolisko', 'puristaa', 'purppura', 'pyhittää', 'pysähtyä', 'rakennus', 'rannikko', 'ratkaisu', 'rauhaisa', 'ravistus', 'riidellä', 'riitaisa', 'rikastua', 'rikkomus', 'ripustaa', 'riutumus', 'ruhtinas', 'rukoilla', 'rusentaa', 'ryöstäjä', 'salainen', 'sammakko', 'selittää', 'seuraava', 'silmukka', 'sisustus', 'sitoumus', 'sitoutua', 'soitanto', 'soittaja', 'sovelias', 'sulattaa', 'suloinen', 'suojella', 'syleillä', 'sytyttää', 'syytetty', 'syyttäjä', 'taipuisa', 'taistelu', 'takaisin', 'takertua', 'taluttaa', 'tapahtua', 'tasainen', 'temppeli', 'tiheikkö', 'timantti', 'todistus', 'toimitus', 'toteutua', 'uskallus', 'uudistua', 'vaikutus', 'vakuutus', 'valistus', 'valkaisu', 'valtikka', 'valvonta', 'vapautua', 'vapautus', 'varistaa', 'varmasti', 'varoitus', 'vavistus', 'venyttää', 'verhottu', 'vetäytyä', 'vihainen', 'vihastua', 'vihastus', 'vihkimys', 'voimakas', 'vuoristo', 'vähäinen', 'väijytys', 'väistyvä', 'väkevyys', 'välähdys', 'väristys', 'yhdeksän', 'yhteinen', 'yhtäkkiä', 'ylhäinen', 'ylpistyä', 'ymmärrys', 'ymmärtää', 'ystävyys'],
[258, 'alamainen', 'antaminen', 'aterioida', 'edellinen', 'erilainen', 'esikoinen', 'esimerkki', 'etumainen', 'haarniska', 'hahmottua', 'hajaantua', 'halkaista', 'halveksua', 'harhailla', 'harrastaa', 'heikontua', 'hellittää', 'hiljainen', 'horjahtaa', 'huojennus', 'huojentaa', 'huojuttaa', 'huokaista', 'huolehtia', 'huudahtaa', 'hyasintti', 'hyödyttää', 'hämmennys', 'hämmentää', 'hämmästys', 'hämmästyä', 'hätyyttää', 'hävittäjä', 'häväistys', 'ikuisesti', 'ilmestyvä', 'ilmoittaa', 'imarrella', 'istuminen', 'jaakobiin', 'jakaantua', 'johdattaa', 'julmistua', 'jäljennös', 'jäljittää', 'jännittää', 'järjestys', 'järkyttää', 'kaareutua', 'kahdeksan', 'kallistua', 'kaltevuus', 'kannattaa', 'kartuttaa', 'karvainen', 'katkaista', 'katkeruus', 'katsastaa', 'kauhistua', 'kauhistus', 'kaunistus', 'keihästys', 'keihästää', 'keinuttaa', 'kietoutua', 'kiiruhtaa', 'kiivastua', 'kiivastus', 'kilpailla', 'kirjoitus', 'kirkastaa', 'kirkastua', 'kiukustua', 'kokoontua', 'kolkuttaa', 'kompastua', 'kompastus', 'koskettaa', 'kostuttaa', 'kotkottaa', 'kouristaa', 'kouristua', 'kouristus', 'kristalli', 'kuivettua', 'kukoistus', 'kuljettaa', 'kultainen', 'kuninkuus', 'kuohuttaa', 'kuuluttaa', 'kyllästyä', 'kyyhkynen', 'kyyristyä', 'kätkeytyä', 'kääriytyä', 'laajentaa', 'langettaa', 'lannistua', 'laskeutua', 'leikkaaja', 'leiriytyä', 'lepuuttaa', 'liikuttaa', 'linnoitus', 'lohduttaa', 'luottamus', 'luovuttaa', 'lähettäjä', 'menestyvä', 'menetelmä', 'mielistyä', 'miljoonaa', 'muistella', 'muistutus', 'munuainen', 'muodostaa', 'muodostus', 'muotoinen', 'musertava', 'mutkainen', 'myöhemmin', 'neljännes', 'nielaista', 'näkymätön', 'nälkäinen', 'närkästyä', 'ohukainen', 'oleskella', 'onnistuva', 'paimentaa', 'painautua', 'paisuttaa', 'palauttaa', 'paljastaa', 'paljastua', 'palvelija', 'parkaista', 'pelikaani', 'peljästys', 'peljästyä', 'peruuttaa', 'pienentää', 'piiloutua', 'pohjoinen', 'polveutua', 'ponnistaa', 'puhdistua', 'puhkaista', 'puhuminen', 'pullistua', 'punoittaa', 'purjehtia', 'purkautua', 'pysäyttää', 'pyydystää', 'pyöristys', 'päällikkö', 'pääskynen', 'pöyristys', 'rangaista', 'rasvainen', 'ratkaista', 'ratsastaa', 'rautainen', 'rikkoutua', 'ruhjoutua', 'rynnistää', 'salaisuus', 'salamoida', 'sammuttaa', 'seisahtua', 'seitsemän', 'sekaantua', 'sekoittaa', 'sellainen', 'sinkoilla', 'sopimaton', 'suitsutus', 'sulkeutua', 'suloisuus', 'suolainen', 'suoristaa', 'suoristua', 'suorittaa', 'suurentaa', 'suuttumus', 'synkistyä', 'syyllinen', 'säikähdys', 'säikähtää', 'sävyisyys', 'taivuttaa', 'tallentaa', 'tallettaa', 'taltuttaa', 'tapahtuma', 'tarkastaa', 'tarkoitus', 'tarpeeksi', 'tasoittaa', 'tavoittaa', 'teroittaa', 'tervehdys', 'teurastus', 'tiivistyä', 'tilaisuus', 'todistaja', 'toteuttaa', 'tuijottaa', 'tunnustaa', 'tunnustus', 'turmeltua', 'turvautua', 'tuulahdus', 'tyhjentää', 'tyrmistyä', 'tähystäjä', 'tällainen', 'täyttymys', 'täyttämys', 'uudelleen', 'vahvistua', 'vahvistus', 'vaikerrus', 'vaivuttaa', 'vakuuttaa', 'valkaista', 'valkoinen', 'valmistaa', 'valmistua', 'valmistus', 'vapauttaa', 'varoittaa', 'varsinkin', 'vartiosto', 'varusteet', 'vastainen', 'verhoutua', 'vertainen', 'viallinen', 'vierailla', 'viheltävä', 'viimeinen', 'viisastua', 'viivästyä', 'viljavuus', 'villainen', 'virkistyä', 'virkistää', 'viruminen', 'virvoitus', 'viskautua', 'voimistua', 'välkähtää', 'vääristää', 'ympäristö', 'äkillinen'],
[118, 'adjektiivi', 'ainokainen', 'antilooppi', 'auttamaton', 'erikoisuus', 'eristäytyä', 'esikoisuus', 'haavoittaa', 'hajanainen', 'harhaileva', 'harjoittaa', 'heilleovat', 'heittäytyä', 'hiljaisuus', 'hirvittävä', 'horjumaton', 'houkutella', 'huiskuttaa', 'hullaantua', 'huuhtoutua', 'hyväksytty',  'joutuminen', 'jännittävä', 'kaatuminen', 'kantaminen', 'kasvattaja', 'kehittynyt', 'kehuskella', 'kieltäytyä', 'kiinnittää', 'kiristellä', 'kirjoittaa', 'kiukkuinen', 'kiusaantua', 'kolmantena', 'kuningatar', 'kuormittaa', 'kuudentena', 'kuuleminen', 'kuuliainen', 'kuuluttaja', 'kylväminen', 'kääntyillä', 'köyhdyttää', 'lahjoittaa', 'laihduttaa', 'laittomuus', 'lakeudelle', 'lakkauttaa', 'laudoittaa', 'levollinen', 'liekehtivä', 'liittoutua', 'linnoittaa', 'loppumaton', 'lähettiläs', 'lähteminen', 'maalauttaa', 'mehiläinen', 'metsästäjä', 'moninainen', 'muistuttaa', 'määkiminen', 'neljäntenä', 'neuvokkuus', 'nyökytellä', 'näkyväinen', 'näyttäytyä', 'nöyryyttää', 'ojentautua', 'onnellinen', 'osallisuus', 'pakolainen', 'palaaminen', 'petollinen', 'professori', 'puhdistava', 'puolustaja', 'pysyväinen', 'päällystys', 'pöyhkeillä', 'rangaistus', 'ratsastaja', 'rauhoittaa', 'rauhoittua', 'riitaisuus', 'saastainen', 'saastuttaa', 'sikäläinen', 'sprinkleri', 'sukulainen', 'syntyminen', 'syrjäyttää', 'säälimätön', 'tahraantua', 'tarkastaja', 'tarkoittaa', 'tavallinen', 'teollisuus', 'todellinen', 'tuntematon', 'tuommoinen', 'tutkimaton', 'tutkiminen', 'tähystellä', 'uljastella', 'vaikuttava', 'vallitseva', 'valmistaja', 'vastustaja', 'vieraantua', 'viidentenä', 'villitsijä', 'vyöttäytyä', 'yhtäläinen', 'yksinäinen', 'yksityinen', 'ylvästellä']]
