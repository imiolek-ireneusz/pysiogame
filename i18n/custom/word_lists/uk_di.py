# -*- coding: utf-8 -*-

# this is a list of words used by the word builder and word maze games and possibly
# other games built in the future
# these words are mainly most commonly used words in English + some other words
# in each sub-list in the list di first number is a number of words in the sublist
# to aviod counting it every time list is selected
# the sublists are consisting of words with len() of 3 - 10
# I think the way of going about internationalization here would be to create a new list
# with words most commonly used in your language rather than translating this
# I am not sure if they are appriopriate for children, but if anyone is interested we can try to built something more suitable.

di = [
    [74, 'або', 'акт', 'але', 'без', 'був', 'біп', 'вже', 'вже', 'вид', 'все', 'все', 'все', 'все', 'все', 'вік', 'газ',
     'дав', 'два', 'дим', 'для', 'для', 'дощ', 'дух', 'дія', 'зір', 'ком', 'кут', 'лом', 'лід', 'ліс', 'між', 'міс',
     'наш', 'ніж', 'ніс', 'ніч', 'ось', 'очі', 'пух', 'під', 'під', 'пір', 'піт', 'раз', 'рис', 'рок', 'рот', 'рух',
     'рій', 'річ', 'сад', 'сам', 'сам', 'сер', 'сон', 'сон', 'сім', 'так', 'так', 'так', 'там', 'тип', 'тих', 'тих',
     'той', 'тон', 'три', 'хто', 'цар', 'час', 'час', 'час', 'чиї', 'шип']
    , [206, 'база', 'банк', 'бити', 'блеф', 'блок', 'брат', 'брат', 'бруд', 'буде', 'буде', 'будь', 'будь', 'були',
       'було', 'було', 'вага', 'весь', 'взяв', 'взяв', 'вище', 'вниз', 'вода', 'вона', 'вони', 'вони', 'впав', 'вуха',
       'вірш', 'геть', 'геть', 'глюк', 'гори', 'грам', 'граф', 'грип', 'двір', 'день', 'драп', 'друг', 'друк', 'дріт',
       'дуже', 'діра', 'діти', 'жаба', 'жало', 'жити', 'звук', 'звіт', 'зима', 'зміг', 'знав', 'знаю', 'зонд', 'його',
       'його', 'його', 'йшли', 'клан', 'клас', 'клас', 'клей', 'клуб', 'ключ', 'ключ', 'кліп', 'коли', 'коло', 'кора',
       'краб', 'край', 'кран', 'кров', 'крок', 'крок', 'куля', 'кулі', 'кінь', 'леді', 'лезо', 'лижі', 'люди', 'літо',
       'мало', 'мало', 'марш', 'мати', 'матч', 'менш', 'миль', 'мити', 'мова', 'мови', 'може', 'може', 'може', 'може',
       'можу', 'море', 'міра', 'міст', 'небо', 'ноги', 'ноги', 'ноги', 'один', 'один', 'один', 'одяг', 'офіс', 'пара',
       'пара', 'парк', 'перш', 'пили', 'писк', 'пити', 'план', 'плащ', 'плед', 'плуг', 'поле', 'прес', 'приз', 'прод',
       'проп', 'рама', 'рано', 'раси', 'риба', 'рись', 'ритм', 'рука', 'самі', 'сани', 'своп', 'свій', 'світ', 'себе',
       'себе', 'сейф', 'село', 'сенс', 'сила', 'сила', 'скат', 'скит', 'скло', 'слем', 'слиз', 'слот', 'слід', 'слід',
       'смак', 'снип', 'сноб', 'сніг', 'сніг', 'соус', 'спав', 'спад', 'спис', 'став', 'стек', 'стор', 'стіл', 'сума',
       'схил', 'схід', 'такі', 'тест', 'того', 'того', 'тому', 'тому', 'тому', 'трюк', 'тупі', 'тіло', 'удар', 'урод',
       'уряд', 'факт', 'флеш', 'флоп', 'флот', 'фліп', 'хліб', 'хоча', 'хоча', 'цілі', 'ціна', 'чолі', 'чому', 'шанс',
       'шарф', 'шафа', 'шест', 'шини', 'шрам', 'штам', 'щось', 'яйця', 'ігри', 'ідея', 'інші']
    , [305, 'акцій', 'армія', 'блиск', 'блиск', 'боюся', 'брейк', 'бренд', 'брижі', 'бійка', 'білий', 'білка', 'більш',
       'більш', 'важка', 'важко', 'весна', 'вечір', 'взяти', 'вибух', 'вирок', 'виріс', 'влада', 'волан', 'втеча',
       'вчені', 'війна', 'вікна', 'вісім', 'вітер', 'вітер', 'гвинт', 'глина', 'годин', 'голос', 'грант', 'грати',
       'гриль', 'гроші', 'грунт', 'група', 'губка', 'давай', 'двері', 'деякі', 'дзвін', 'дзвін', 'дивно', 'дикий',
       'добре', 'добре', 'довго', 'доказ', 'досяг', 'дошка', 'дошка', 'дрейф', 'дриль', 'друзі', 'дужки', 'думаю',
       'думаю', 'думка', 'екран', 'ескіз', 'ефект', 'жвава', 'життя', 'жінка', 'жінки', 'завод', 'зажим', 'занос',
       'запах', 'запис', 'зараз', 'захід', 'заяву', 'зброя', 'земля', 'земля', 'зерно', 'знизу', 'знову', 'зірка',
       'зірки', 'зірки', 'карта', 'квіти', 'кисть', 'клерк', 'клоун', 'книга', 'князь', 'кожен', 'кожен', 'колір',
       'комах', 'краще', 'криза', 'крила', 'круто', 'купив', 'кухар', 'кішка', 'ласка', 'лаяти', 'легко', 'лежав',
       'листи', 'ложка', 'любов', 'ляпас', 'ліжко', 'лінія', 'літак', 'мазок', 'майже', 'майор', 'малий', 'марка',
       'межах', 'менше', 'метал', 'метод', 'мозок', 'морда', 'мороз', 'морок', 'місто', 'місто', 'місце', 'місце',
       'мітла', 'набір', 'надія', 'назад', 'народ', 'науку', 'нести', 'нижче', 'новий', 'носик', 'одягу', 'озеро',
       'океан', 'опіки', 'осінь', 'палях', 'папір', 'парші', 'пасмо', 'писав', 'плече', 'плеєр', 'плита', 'плити',
       'плоть', 'пляма', 'пляма', 'пляма', 'пляму', 'побіг', 'повна', 'повне', 'поділ', 'політ', 'поруч', 'поруч',
       'потік', 'похід', 'почав', 'почав', 'почув', 'поїзд', 'право', 'проте', 'проте', 'проти', 'прямі', 'птиці',
       'пункт', 'після', 'після', 'пісня', 'пісок', 'пішли', 'радий', 'радіо', 'разом', 'разом', 'років', 'рости',
       'рукав', 'рядок', 'рядок', 'рівні', 'різні', 'різні', 'річка', 'светр', 'свині', 'свист', 'серце', 'синку',
       'синяк', 'синій', 'сквош', 'скелі', 'скотч', 'скунс', 'слайд', 'сливи', 'слова', 'сліпи', 'смуга', 'смуга',
       'совок', 'сонце', 'спина', 'спліт', 'спорт', 'спрей', 'стадо', 'сталь', 'стані', 'стати', 'стейк', 'стиль',
       'стояв', 'страх', 'страх', 'струм', 'стіна', 'сухий', 'сфера', 'сходи', 'схоже', 'сцена', 'сюжет', 'сірий',
       'сітка', 'такий', 'таким', 'також', 'танці', 'темно', 'тепло', 'тихий', 'тонкі', 'точка', 'точно', 'трава',
       'троль', 'тромп', 'трохи', 'труба', 'тріск', 'убиті', 'увагу', 'угода', 'умови', 'фарба', 'ферма', 'флекс',
       'форма', 'фраза', 'фільм', 'філія', 'філії', 'халат', 'хвилі', 'хвіст', 'хмара', 'хрест', 'хтось', 'цегла',
       'центр', 'цифра', 'цукор', 'цього', 'часом', 'часто', 'через', 'через', 'череп', 'чином', 'число', 'числі',
       'човен', 'шалот', 'шахта', 'шифер', 'школа', 'шкіри', 'шпиль', 'шпори', 'шприц', 'штамп', 'шторм', 'шукач',
       'шість', 'ялина', 'ясний', 'іноді', 'іскру']
    ,
    [277, 'аварія', 'багато', 'багато', 'багато', 'багато', 'батько', 'бачили', 'бачите', 'блеать', 'блузка', 'болото',
     'брехня', 'бронза', 'будучи', 'бігати', 'бізнес', 'вдарив', 'вдарив', 'велика', 'вереск', 'вереск', 'верхня',
     'весело', 'взуття', 'висоти', 'виявив', 'вкриті', 'вміння', 'вогонь', 'водити', 'ворона', 'вперед', 'вперед',
     'вправи', 'вранці', 'вулиця', 'вулиці', 'відчув', 'військ', 'вітати', 'гладка', 'глобус', 'голова', 'голови',
     'гордий', 'гравій', 'графік', 'грубий', 'грудку', 'далеко', 'далекі', 'двигун', 'дерева', 'дерево', 'дерево',
     'десять', 'деталі', 'дизайн', 'дитина', 'дитина', 'добрий', 'довіра', 'догляд', 'додати', 'додому', 'доктор',
     'долари', 'долини', 'дорога', 'досвід', 'дракон', 'другий', 'дюймах', 'дядько', 'дійсно', 'жовтий', 'завжди',
     'залізо', 'землею', 'змійка', 'знайти', 'золото', 'зразок', 'зробив', 'зробив', 'кабіна', 'кажучи', 'кажучи',
     'камінь', 'капати', 'квітка', 'кидати', 'кисень', 'клімат', 'ковдру', 'колеса', 'корита', 'корови', 'корона',
     'корінь', 'котися', 'крапля', 'красти', 'кращий', 'країна', 'крикет', 'крихта', 'кричав', 'круглі', 'крутий',
     'купити', 'кутова', 'кіготь', 'кілька', 'кілька', 'кільце', 'кінець', 'кістки', 'латунь', 'лебідь', 'липкий',
     'людина', 'людина', 'літати', 'машина', 'машину', 'минуле', 'могила', 'мокрий', 'молоді', 'молоко', 'молоти',
     'молюск', 'момент', 'музика', 'муліне', 'місяць', 'навіть', 'натовп', 'низько', 'носити', 'нюхати', 'ніколи',
     'ніколи', 'нічого', 'опухлі', 'острів', 'оцінка', 'пагорб', 'палити', 'палиці', 'пальці', 'панчіх', 'партія',
     'пастка', 'певний', 'період', 'пишіть', 'планка', 'плаття', 'плоскі', 'плюнув', 'повний', 'повінь', 'погане',
     'погляд', 'погляд', 'погода', 'пожежа', 'позаду', 'посаду', 'послав', 'похила', 'почати', 'почути', 'правда',
     'правда', 'прапор', 'приніс', 'провів', 'проект', 'проект', 'прокат', 'просто', 'просто', 'процес', 'прямий',
     'півдні', 'північ', 'підйом', 'піднос', 'підняв', 'равлик', 'раптом', 'робота', 'робота', 'рогата', 'розділ',
     'розмір', 'розуму', 'розуму', 'рівень', 'рідини', 'свіжий', 'світло', 'сестра', 'сиділи', 'сидіти', 'сказав',
     'сказав', 'склади', 'скупий', 'скутер', 'сльота', 'сліпий', 'сморід', 'сміття', 'собака', 'солома', 'сотень',
     'спалах', 'спалах', 'список', 'сплеск', 'спосіб', 'спринт', 'старий', 'статуя', 'стебло', 'стежка', 'стерео',
     'стогін', 'стояти', 'страйк', 'стрейч', 'стібка', 'суфікс', 'сіркою', 'тасьма', 'теплий', 'тисячі', 'товсті',
     'третій', 'тримав', 'трубка', 'тільки', 'флейта', 'форель', 'фрукти', 'фунтів', 'фігура', 'фільтр', 'хвилин',
     'хочете', 'хребет', 'худоба', 'цвісти', 'центів', 'церква', 'цілком', 'чистий', 'читати', 'членів', 'чорний',
     'чотири', 'чханні', 'шахрай', 'швидко', 'швидко', 'швидкі', 'широка', 'шлунка', 'шпигун', 'щілину', 'яблуко',
     'інакше', 'їздити']
    ,
    [245, 'бавовна', 'бавовна', 'багатий', 'бажання', 'бакалія', 'барабан', 'барабан', 'бахрома', 'благати', 'близько',
     'близько', 'борошно', 'бродяга', 'брязкіт', 'будинок', 'бульйон', 'бітрейт', 'важливі', 'вдарити', 'ведмідь',
     'великий', 'великий', 'великий', 'великий', 'взагалі', 'вибрати', 'виводок', 'випадок', 'вирвати', 'вирвати',
     'виросли', 'вирішив', 'високий', 'високий', 'висівки', 'волосся', 'втратив', 'вчитель', 'відомий', 'відомий',
     'вільний', 'вільний', 'вітрило', 'гармонь', 'гарячий', 'гладкий', 'говорив', 'голосно', 'горбаль', 'гострий',
     'готовий', 'гілочка', 'давайте', 'держава', 'дихання', 'доверху', 'довести', 'довжина', 'дружина', 'дряпати',
     'енергія', 'жорсткі', 'закуски', 'замість', 'занадто', 'запитав', 'заставу', 'затишно', 'звисати', 'зелений',
     'зламані', 'зловили', 'зловити', 'змінити', 'змішати', 'знайшов', 'зокрема', 'зробити', 'кабінет', 'капелюх',
     'капітал', 'капітан', 'картини', 'квадрат', 'клапоть', 'клітини', 'ковзнув', 'ковтати', 'колиска', 'колонка',
     'команда', 'коробку', 'короткі', 'красива', 'кремінь', 'кричати', 'кімната', 'личинка', 'ліворуч', 'ліжечка',
     'магазин', 'магазин', 'малював', 'масштаб', 'матерія', 'мелодія', 'мовчить', 'можливо', 'можливо', 'можливо',
     'молитва', 'морські', 'мотузка', 'мільйон', 'містять', 'місяців', 'навколо', 'навпаки', 'наземні', 'нарешті',
     'нарешті', 'настрій', 'насіння', 'недолік', 'носилки', 'область', 'область', 'обличчя', 'обробка', 'означає',
     'окремий', 'олівець', 'описати', 'осколок', 'отримав', 'отримав', 'падіння', 'переляк', 'печіння', 'питання',
     'плавали', 'плавати', 'плакала', 'плакати', 'планета', 'планети', 'платять', 'побачив', 'повзати', 'повидло',
     'повинні', 'повинні', 'повинні', 'поворот', 'повірте', 'повітря', 'поганий', 'поганий', 'полетів', 'похвала',
     'почуття', 'поїздка', 'поїхали', 'правило', 'прийшов', 'причина', 'приємно', 'провину', 'продати', 'продукт',
     'продукт', 'пройшло', 'простір', 'пустеля', 'південь', 'підлогу', 'підняли', 'пізніше', 'ремесла', 'решітка',
     'розбити', 'розливу', 'рослини', 'рівнини', 'різниця', 'рішення', 'свинець', 'сильний', 'символи', 'системи',
     'скажімо', 'сказати', 'складки', 'складні', 'скребок', 'словник', 'служити', 'слухати', 'смажити', 'сміявся',
     'солдати', 'співати', 'стадіон', 'станція', 'степлер', 'стовбур', 'сторона', 'строгий', 'струмок', 'струмок',
     'струмок', 'струнка', 'стійкий', 'стілець', 'сутичка', 'танчики', 'тварини', 'терміни', 'тиждень', 'тканина',
     'тримати', 'тримати', 'троянди', 'тріщини', 'тупають', 'увійшов', 'фабрики', 'фактори', 'фермери', 'фракція',
     'фізичні', 'хлопчик', 'холодно', 'хропіти', 'цибуля-', 'частина', 'частини', 'чоловік', 'чудовий', 'широкий',
     'щасливі', 'іменник', 'інсульт', 'історія', 'історія']
    , [173, 'блимають', 'блошиний', 'боротьба', 'боротьба', 'бродячих', 'вантажні', 'вартість', 'веснянки', 'вимовити',
       'виноград', 'виноград', 'винятком', 'вирізати', 'вирішити', 'витягнув', 'вказують', 'відверто', 'відсотки',
       'відчуваю', 'гарчання', 'гвоздику', 'глибокий', 'говорити', 'говорити', 'годинник', 'годинник', 'гойдалки',
       'головний', 'головний', 'головний', 'голосний', 'гордість', 'діаграма', 'дівчинка', 'дієслово', 'елементи',
       'заварити', 'зазвичай', 'зайнятий', 'заковика', 'залишити', 'заметіль', 'застібка', 'зауважте', 'західний',
       'зверніть', 'звичайна', 'звичайно', 'згорнути', 'зламався', 'зроблено', 'зупинити', 'зупинити', 'ймовірно',
       'кальмари', 'каракуль', 'каракулі', 'каркання', 'кататися', 'ковзанах', 'ковзання', 'ковзання', 'компанію',
       'контроль', 'корабель', 'красивий', 'крастися', 'крендель', 'крихітні', 'крохмаль', 'культури', 'ліхтарик',
       'малювати', 'молекули', 'молитися', 'мустанга', 'належать', 'налякати', 'написано', 'напрямок', 'наречена',
       'невелике', 'негідник', 'обробкою', 'обрізати', 'обіцянку', 'оснастки', 'основний', 'особливо', 'отримати',
       'паросток', 'пасуться', 'передати', 'передній', 'перемога', 'персонал', 'плямочка', 'по-друге', 'по-перше',
       'поверхню', 'повільно', 'повільно', 'подорожі', 'показано', 'показати', 'полуниця', 'поодинці', 'поплавок',
       'порожній', 'посипати', 'посмішка', 'посмішка', 'поспішна', 'поставку', 'потрібно', 'похмурим', 'пояснити',
       'практика', 'практика', 'прибутку', 'принести', 'принцеса', 'пристрій', 'причиною', 'проблема', 'проблеми',
       'провисає', 'програма', 'продукти', 'продукти', 'пропелер', 'професор', 'північна', 'підводне', 'піднявся',
       'ремінець', 'ретельно', 'речовини', 'розумний', 'рівняння', 'священик', 'світіння', 'селезень', 'середній',
       'сильніше', 'скибочку', 'солодкий', 'спритний', 'спідниця', 'століття', 'стремено', 'стрибали', 'стрибати',
       'стрижень', 'стриптиз', 'студенти', 'сучасний', 'схопився', 'сценарій', 'сьогодні', 'тащаться', 'тендітна',
       'торгівля', 'хоробрий', 'цвітіння', 'цінність', 'червоний', 'черствий', 'чоловіки', 'штовхнув', 'штурмове',
       'яскравий', 'інвентар']
    , [98, 'благодать', 'блондинка', 'бринькати', 'більшість', 'визначити', 'виробляти', 'висловити', 'витрачати',
       'включають', 'всередині', 'відблиски', 'відкритий', 'відповідь', 'гарчанням', 'гребінець', 'допомогти',
       'достатньо', 'дізнатися', 'забивають', 'завивають', 'загальний', 'займенник', 'заповнені', 'захистити',
       'зберігати', 'збільшити', 'звиватися', 'здавалося', 'здавалося', 'зрозуміти', 'зчеплення', 'зчеплення',
       'зіпсувати', 'зіткнення', 'клікнувши', 'комутатор', 'копіювати', 'крадучись', 'кукурудза', 'кількість',
       'лікування', 'майнового', 'маленький', 'малювання', 'мастильні', 'матеріали', 'мистецтво', 'наприклад',
       'наприклад', 'наречений', 'народився', 'насправді', 'насправді', 'натисніть', 'необхідно', 'нишпорити',
       'одягнений', 'оселилися', 'особливий', 'очікувати', 'перевірте', 'пластівці', 'погодився', 'подряпини',
       'полювання', 'порівняти', 'потрібним', 'почекайте', 'починаючи', 'поширення', 'правильно', 'правильно',
       'президент', 'претензії', 'природний', 'прокрутки', 'процідити', 'підписати', 'підірвали', 'результат',
       'розвідник', 'розгортки', 'розділені', 'рукавички', 'сенсорний', 'сковороді', 'сутулість', 'трапилося',
       'трикутник', 'тушкувати', 'тушкувати', 'узбережжя', 'укладений', 'упевнений', 'управляти', 'чорнослив',
       'чіплятися', 'швидкість']
    ,
    [53, 'автомобіль', 'благослови', 'вантажівка', 'величезний', 'волосистої', 'встановити', 'відбілювач', 'гальмівний',
     'голодувати', 'гравітація', 'дозволяють', 'доповнення', 'друкованої', 'електричні', 'жадібність', 'забруднень',
     'заклинання', 'залишитися', 'заморожені', 'захоплення', 'здивування', 'здивування', 'зустрітися', 'коричневий',
     'косоокість', 'найближчим', 'неглибокої', 'перемішати', 'переміщати', 'побудувати', 'повернення', 'повзучості',
     'потертості', 'потужність', 'потягнувся', 'прикметник', 'припустимо', 'прогулянка', 'пропустити', 'протектора',
     'розглянути', 'розроблені', 'самостійно', 'сканування', 'сонливість', 'спробувати', 'стабільний', 'створювати',
     'сьогодення', 'тривалість', 'тримайтеся', 'фотографія', 'харчування']]
