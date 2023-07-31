import telebot
from telebot import types
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup

from streets import inline_street
from selenium_logic import open_space, add_info, search, dclose


bot = telebot.TeleBot('6326447739:AAFrNGvl3HGSq1uUQEoCzzaeXer1eJd8EC4')


markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
add_u = types.KeyboardButton('/add_user')
get_ready_uesrs = types.KeyboardButton('/users')
markup.row(add_u, get_ready_uesrs)


@bot.message_handler(commands=['start'])
def start_message(message: types.Message):
    bot.send_message(message.from_user.id, 'Бот для создание аккаунтов Умныного дома', reply_markup=markup)


@bot.message_handler(commands=['users'])
def get_users(message: types.Message):
    msg = bot.send_message(
        message.from_user.id,
        'Выберите улицу',
        reply_markup=inline_street
        )
    bot.register_next_step_handler(msg, get_street)


@bot.callback_query_handler(lambda call: True)
def get_street(call: types.CallbackQuery):
    open_space()
    st = search(call.data)
    for i in st:
        bot.send_message(call.from_user.id, i)
    dclose()


@bot.message_handler(commands=['add_user'])
def add_user(message: types.Message):
    global add_dict
    add_dict = dict()
    
    inline_city = InlineKeyboardMarkup(row_width=1)
    bish = InlineKeyboardButton(text='Бишкек', callback_data='г. Бишкек')
    inline_city.row(bish)

    bot.send_message(message.chat.id, "Выберите город", reply_markup=inline_city)
    bot.send_message('-994090707', f'{message.from_user.full_name}\n{message.from_user.username}\
                     \nНачал регистрацию')


@bot.callback_query_handler(lambda call: call.data == "г. Бишкек")
def city(call: types.CallbackQuery):
    add_dict['city'] = call.data
    bot.send_message(call.from_user.id, "Выберите улицу", reply_markup=inline_street)


@bot.callback_query_handler(lambda call: True)
def street(call: types.CallbackQuery):
    add_dict['street'] = call.data
    msg = bot.send_message(call.from_user.id, "Напишите номер дома")
    bot.register_next_step_handler(msg, house)


def house(message: types.Message):
    add_dict['house'] = message.text
    msg = bot.send_message(message.chat.id, "Напишите номер подъезда")
    bot.register_next_step_handler(msg, ent)



def ent(message: types.Message):
    if message.text.isdigit():
        add_dict['ent'] = message.text
        msg = bot.send_message(message.chat.id, "Напишите номер этажа")
        bot.register_next_step_handler(msg, floor)
    else:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Вы ввели букв, напишите снова"), ent)


def floor(message: types.Message):
    if message.text.isdigit():
        add_dict['floor'] = message.text
        msg = bot.send_message(message.chat.id, "Напишите номер квартиры")
        bot.register_next_step_handler(msg, appart)
    else:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Вы ввели букв, напишите снова"), appart)


def appart(message: types.Message):
    add_dict['appart'] = message.text
    msg = bot.send_message(message.chat.id, "Напишите имя")
    bot.register_next_step_handler(msg, name)


def name(message: types.Message):
    if message.text.isalpha():
        add_dict['name'] = message.text
        msg = bot.send_message(message.chat.id, "Напишите фамилию")
        bot.register_next_step_handler(msg, last_name)
    else:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Вы ввели цифру, напишите снова"), name)


def last_name(message: types.Message):
    if message.text.isalpha():
        add_dict['name'] = f'{add_dict.get("name")} {message.text}'
        msg = bot.send_message(message.chat.id, "Напишите номер телефона в формате: 707901901")
        bot.register_next_step_handler(msg, phone_num)
    else:
        bot.register_next_step_handler(bot.send_message(message.chat.id, "Вы ввели цифру, напишите снова"), last_name)


def phone_num(message: types.Message):
    num = message.text
    if len(num) == 9:
        add_dict['phone_num'] = f'+996{num}'
        msg = bot.send_message(message.chat.id, "Напишите примечание")
        bot.register_next_step_handler(msg, request)
    else:
        msg = bot.send_message(message.chat.id, "Вы ввели не правильный номер, введите его заново")
        bot.register_next_step_handler(msg, phone_num)


def request(message: types.Message):
    add_dict['requests'] = message.text
    inline_status = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    done = types.KeyboardButton(text='Оформить заявку')
    exc = types.KeyboardButton(text='Сбросить')
    inline_status.row(done, exc)

    msg = bot.send_message(message.chat.id, f"Проверьте данные\nФИО: {add_dict.get('name')}\
                        \nГород: {add_dict.get('city')}\
                        \nУлица: {add_dict.get('street')}\nДом: {add_dict.get('house')}\
                        \nПодъезд: {add_dict.get('ent')}\nЭтаж: {add_dict.get('floor')}\
                        \nКвартира: {add_dict.get('appart')}\nНомер телефона: {add_dict.get('phone_num')}\
                        Примечание: {add_dict.get('requests')}", 
                        reply_markup=inline_status)
    bot.register_next_step_handler(msg, status)
    


@bot.callback_query_handler(lambda call: call.data == 'Оформить заявку')
def status(message: types.Message):
    if message.text == 'Оформить заявку':
        try:
            open_space()
            ls = add_info(add_dict)
            bot.send_message(message.from_user.id, f'Заявка офромлена: лс абонента {ls}', reply_markup=markup)
            bot.send_message('-994090707', f'{message.from_user.full_name},\
                             \n{message.from_user.username}\nЛС: {ls}')
        except ZeroDivisionError:
            bot.send_message(message.from_user.id, f'Пользователь существует, проверьте данные', reply_markup=markup)
    else:
        bot.send_message(message.from_user.id, f'Вы сбросили данные', reply_markup=markup)
    

bot.infinity_polling()
