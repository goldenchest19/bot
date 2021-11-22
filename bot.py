import telebot
import configure
from telebot import types

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(commands=['get_info', 'info', 'start'])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_yes = types.InlineKeyboardButton(text='ДА', callback_data='yes')
    item_no = types.InlineKeyboardButton(text='НЕТ', callback_data='no')
    # item_go = types.InlineKeyboardButton(text='отправиться в путешествие', callback_data='go')

    markup_inline.add(item_yes, item_no)
    client.send_message(message.chat.id, 'Желаете попасть к нам в компанию?', reply_markup=markup_inline)


@client.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == 'yes':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_id = types.KeyboardButton('МОЙ ID')
        item_username = types.KeyboardButton('МОЙ НИК')

        markup_reply.add(item_id, item_username)
        client.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
                            reply_markup=markup_reply)
    elif call.data == 'no':
        pass
    elif call.data == 'go':
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item_moscow = types.KeyboardButton('Travel to Moscow')
        item_SPB = types.KeyboardButton('Travel to SPB')

        markup_reply.add(item_moscow, item_SPB)
        client.send_message(call.message.chat.id, 'Нажмите на одну из кнопок',
                            reply_markup=markup_reply)

    client.answer_callback_query(callback_query_id=call.id)


@client.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'МОЙ ID':
        client.send_message(message.chat.id, f'Your ID: {message.from_user.id}')
    elif message.text == 'МОЙ НИК':
        client.send_message(message.chat.id, f'Your username: {message.from_user.first_name}')
    elif message.text == 'Travel to SPB':
        client.send_message(message.chat.id,
                            f'Ознакомиться с путевками можно по тут https://www.coral.ru/main/russia/tury-v-sanktpeterburg-na-dvoih/')
    elif message.text == 'Travel to Moscow':
        client.send_message(message.chat.id,
                            f'Ознакомиться с интересными местами можно по тут https://kudago.com/msk/list/samye-interesnye-mesta-v-moskve/')


client.polling(none_stop=True, interval=0)
