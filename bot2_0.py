import telebot
import configure
from telebot import types

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(commands=["aplication"])
def aplication(message):
    rmk = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    rmk.add(types.KeyboardButton("Да"), types.KeyboardButton("Нет"))

    msg = client.send_message(message.chat.id, "Желаете попасть к нам в компанию?", reply_markup=rmk)
    client.register_next_step_handler(msg, user_answer)

    types.ReplyKeyboardRemove(selective=False)


def user_answer(message):
    if message.text == "Да":
        msg = client.send_message(message.chat.id, "На какую позицию вы претендуете?")
        client.register_next_step_handler(msg, user_position)
    elif message.text == "Нет":
        client.send_message(message.chat.id, "Всего доброго!")


def user_position(message):
    position = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    position.add(types.KeyboardButton("Java-разработчик"), types.KeyboardButton("HR"),
                 types.KeyboardButton("IOS-разработчик"), types.KeyboardButton("DevOps-инженер"),
                 types.KeyboardButton("Уборщик")
                 )

    position = client.send_message(message.chat.id, "Желаете попасть к нам в компанию??????", reply_markup=position)
    client.register_next_step_handler(position, user_position)

    types.ReplyKeyboardRemove(selective=False)


def user_position(message):
    client.send_message(message.chat.id, "супер")


client.polling(none_stop=True, interval=0)
