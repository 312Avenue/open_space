from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

inline_street = InlineKeyboardMarkup(row_width=3)

# Улицы
tokt = InlineKeyboardButton(text='ул. Токтоналиева', callback_data='ул. Токтоналиева')
aprel = InlineKeyboardButton(text='ул. 7-апреля', callback_data='ул. 7-апреля')
abaya = InlineKeyboardButton(text='ул. Абая', callback_data='ул. Абая')

inline_street.row(aprel, abaya)

abdrakhahman = InlineKeyboardButton(text='ул. Абдрахманова', callback_data='ул. Абдрахманова')
abdymomun = InlineKeyboardButton(text='ул. Абдумомунова', callback_data='ул. Абдумомунова')
aj_baatyr = InlineKeyboardButton(text='ул. Ажыбек Баатыра', callback_data='ул. Ажыбек Баатыра')

inline_street.row(abdrakhahman, abdymomun)

ayni = InlineKeyboardButton(text='ул. Айни', callback_data='ул. Айни')
akylbek = InlineKeyboardButton(text='ул. Акылбекова', callback_data='ул. Акылбекова')
ankara = InlineKeyboardButton(text='ул. Анкара', callback_data='ул. Анкара')

inline_street.row(ayni, akylbek, ankara)

arst_duysh = InlineKeyboardButton(text='ул. Арстанбека Дуйшеева', callback_data='ул. Арстанбека Дуйшеева')

inline_street.row(aj_baatyr, arst_duysh)

vinograd = InlineKeyboardButton(text='ул. Виноградная', callback_data='ул. Виноградная')
grazhdan = InlineKeyboardButton(text='ул. Гражданская', callback_data='ул. Гражданская')
griboedov = InlineKeyboardButton(text='ул. Грибоедова', callback_data='ул. Грибоедова')

inline_street.row(vinograd, grazhdan, griboedov)

jal_15 = InlineKeyboardButton(text='ул. Джал-15', callback_data='ул. Джал-15')
jal_23 = InlineKeyboardButton(text='ул. Джал-23', callback_data='ул. Джал-23')
jal_29 = InlineKeyboardButton(text='ул. Джал-29', callback_data='ул. Джал-29')

inline_street.row(jal_15, jal_23, jal_29)

jal_artis = InlineKeyboardButton(text='ул. Джал-Артис', callback_data='ул. Джал-Артис')
djambaeva = InlineKeyboardButton(text='ул. Джаманбаева', callback_data='ул. Джаманбаева')

inline_street.row(jal_artis, djambaeva)

djantosh = InlineKeyboardButton(text='ул. Джантошева', callback_data='ул. Джантошева')
djunushaliev = InlineKeyboardButton(text='ул. Джунусалиева', callback_data='ул. Джунусалиева')

inline_street.row(djantosh, djunushaliev)

joomart_bokonb = InlineKeyboardButton(text='ул. Жоомарта Боконбаева', callback_data='ул. Жоомарта Боконбаева')
jukeeva_pudov = InlineKeyboardButton(text='ул. Жукеева Пудовкина', callback_data='ул. Жукеева Пудовкина')

inline_street.row(joomart_bokonb, jukeeva_pudov)

zagorod = InlineKeyboardButton(text='ул. Загорская', callback_data='ул. Загорская')
ibraimov = InlineKeyboardButton(text='ул. Ибраимова', callback_data='ул. Ибраимова')

inline_street.row(zagorod, ibraimov)

akhunbaev = InlineKeyboardButton(text='ул. Исы Ахунбаева', callback_data='ул. Исы Ахунбаева')
kalyk_ak = InlineKeyboardButton(text='ул. Калыка Акиева', callback_data='ул. Калыка Акиева')

inline_street.row(akhunbaev, kalyk_ak)

kara_kul = InlineKeyboardButton(text='ул. Кара-Кульская', callback_data='ул. Кара-Кульская')
kiyizb = InlineKeyboardButton(text='ул. Кийизбаевой', callback_data='ул. Кийизбаевой')

inline_street.row(kara_kul, kiyizb)

kok_jar = InlineKeyboardButton(text='ул. Кок-Жар', callback_data='ул. Кок-Жар')
kuyruchuk = InlineKeyboardButton(text='ул. Куйручук', callback_data='ул. Куйручук')

inline_street.row(kok_jar, kuyruchuk)

kyrk_kys = InlineKeyboardButton(text='ул. Кырк-Кыз', callback_data='ул. Кырк-Кыз')
lion_tolst = InlineKeyboardButton(text='ул. Льва Толстого', callback_data='ул. Льва Толстого')

inline_street.row(kyrk_kys, lion_tolst)

maldybaev = InlineKeyboardButton(text='ул. Малдыбаева', callback_data='ул. Малдыбаева')
manas = InlineKeyboardButton(text='ул. Манаса', callback_data='ул. Манаса')

inline_street.row(maldybaev, manas)

masaliev = InlineKeyboardButton(text='ул. Масалиева', callback_data='ул. Масалиева')
mederov = InlineKeyboardButton(text='ул. Медерова', callback_data='ул. Медерова')

inline_street.row(masaliev, mederov)

moldokulov = InlineKeyboardButton(text='ул. Молдокулова', callback_data='ул. Молдокулова')
moskov = InlineKeyboardButton(text='ул. Московская', callback_data='ул. Московская')

inline_street.row(moldokulov, moskov)

isanov = InlineKeyboardButton(text='ул. Насирдина Исанова', callback_data='ул. Насирдина Исанова')
orozbek = InlineKeyboardButton(text='ул. Орозбекова', callback_data='ул. Орозбекова')

inline_street.row(isanov, orozbek)

panfil = InlineKeyboardButton(text='ул. Панфилова', callback_data='ул. Панфилова')
razzak = InlineKeyboardButton(text='ул. Раззакова', callback_data='ул. Раззакова')

inline_street.row(panfil, razzak)

sagyndyk = InlineKeyboardButton(text='ул. Сагындыкова Таланта', callback_data='ул. Сагындыкова Таланта')
sayak = InlineKeyboardButton(text='ул. Саякбая Каралаева', callback_data='ул. Саякбая Каралаева')

inline_street.row(sagyndyk, sayak)

skryab = InlineKeyboardButton(text='ул. Скрябина', callback_data='ул. Скрябина')
suerkul = InlineKeyboardButton(text='ул. Суеркулова', callback_data='ул. Суеркулова')
sydyk = InlineKeyboardButton(text='ул. Сыдыкова', callback_data='ул. Сыдыкова')

inline_street.row(skryab, suerkul, sydyk)

tybysh = InlineKeyboardButton(text='ул. Табышалиева', callback_data='ул. Табышалиева')
termech = InlineKeyboardButton(text='ул. Термечикова', callback_data='ул. Термечикова')

inline_street.row(tybysh, termech)

toktogul = InlineKeyboardButton(text='ул. Токтогула', callback_data='ул. Токтогула')
termech = InlineKeyboardButton(text='ул. Термечикова', callback_data='ул. Термечикова')

inline_street.row(toktogul, termech)

tugolbai = InlineKeyboardButton(text='ул. Туголбай-Ата', callback_data='ул. Туголбай-Ата')
turusbek = InlineKeyboardButton(text='ул. Турусбекова', callback_data='ул. Турусбекова')

inline_street.row(tugolbai, turusbek)

tynaliev = InlineKeyboardButton(text='ул. Тыналиева', callback_data='ул. Тыналиева')
umetaliev = InlineKeyboardButton(text='ул. Уметалиева', callback_data='ул. Уметалиева')

inline_street.row(tynaliev, umetaliev)

ulan = InlineKeyboardButton(text='ул. Улан', callback_data='ул. Улан')
uchkun = InlineKeyboardButton(text='ул. Учкун', callback_data='ул. Учкун')
frunze = InlineKeyboardButton(text='ул. Фрунзе', callback_data='ул. Фрунзе')

inline_street.row(ulan, uchkun, frunze)

fatiyan = InlineKeyboardButton(text='ул. Фатьянова', callback_data='ул. Фатьянова')
chuikov = InlineKeyboardButton(text='ул. Чуйкова', callback_data='ул. Чуйкова')

inline_street.row(fatiyan, chuikov)

shevchenko = InlineKeyboardButton(text='ул. Шевченко', callback_data='ул. Шевченко')
elebaev = InlineKeyboardButton(text='ул. Элебаева', callback_data='ул. Элебаева')

inline_street.row(shevchenko, elebaev)

fuchik = InlineKeyboardButton(text='ул. Юлиуса Фучика', callback_data='ул. Юлиуса Фучика')
unusaliev = InlineKeyboardButton(text='ул. Юнусалиева', callback_data='ул. Юнусалиева')

inline_street.row(fuchik, unusaliev)

logvinenko = InlineKeyboardButton(text='ул. Якова Логвиненко', callback_data='ул. Якова Логвиненко')

inline_street.row(logvinenko, tokt)

# Микрорайоны
mkrAs =InlineKeyboardButton(text='Асанбай', callback_data='мкр. Асанбай') 
mkrVerJal =InlineKeyboardButton(text='Верхний Джал', callback_data='мкр. Верхний Джал') 
mkrTun =InlineKeyboardButton(text='Тунгуч', callback_data='мкр. Тунгуч') 
mkrTun =InlineKeyboardButton(text='Тунгуч', callback_data='мкр. Тунгуч') 
mkr4 = InlineKeyboardButton(text='4 мкр', callback_data='мкр. 4')
mkr8 = InlineKeyboardButton(text='8 мкр', callback_data='мкр. 8')
mkr11 = InlineKeyboardButton(text='11 мкр', callback_data='мкр. 11')
mkr12 = InlineKeyboardButton(text='12 мкр', callback_data='мкр, 12')

inline_street.row(mkr11, mkr12, mkr4, mkr8)
inline_street.row(mkrAs, mkrTun, mkrVerJal)