import requests
import telebot
from bs4 import BeautifulSoup
from telebot import types

import configure

client = telebot.TeleBot(configure.config['token'])


@client.message_handler(commands=["start", "home"])
def get_user_info(message):
    markup_inline = types.InlineKeyboardMarkup()
    item_lastNews = types.InlineKeyboardButton(text='интересные статьи', callback_data='N')
    item_AllLastNews = types.InlineKeyboardButton(text='последние новости', callback_data='ALL')
    item_ChanelLastNews = types.InlineKeyboardButton(text='найти статью', callback_data='CHNEWS')

    markup_inline.add(item_lastNews, item_AllLastNews, item_ChanelLastNews)
    client.send_message(message.chat.id, 'Здравствуйте, я информационный бот портал ХАБР!'
                                         '\nНа данный момент я умею присылать последние публикации из самых обсуждаемых тем, последние новости непосредственно портала ХАБР. '
                                         'А также последние новости определенного информационного портала',
                        reply_markup=markup_inline
                        )


@client.callback_query_handler(func=lambda call: True)
def answer(call):
    if call.data == "N":
        markup_reply = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
        item_AI = types.KeyboardButton('AI')
        item_DS = types.KeyboardButton('DS')
        item_CryprtoNews = types.KeyboardButton('Crypto News')
        item_NFT = types.KeyboardButton('NFT')
        item_WD = types.KeyboardButton('web-design')
        item_algoritm = types.KeyboardButton('алгоритмы')

        markup_reply.row(item_AI, item_DS, item_CryprtoNews)
        markup_reply.row(item_NFT, item_WD, item_algoritm)
        client.send_message(call.message.chat.id, 'Выберете интересующее вас направление'
                                                  'и я пришлю вам последние 10 статей на эту тему',
                            reply_markup=markup_reply
                            )
    elif call.data == 'ALL':
        url = 'https://habr.com/ru/news/'
        request = requests.get(url)
        bs = BeautifulSoup(request.text, "html.parser")
        all_links = bs.find_all("a", class_="tm-article-snippet__title-link")
        count = 0
        for link in all_links:
            sdk = "https://habr.com" + link["href"]
            client.send_message(call.message.chat.id, sdk)
            count += 1
            if count == 10:
                break
        client.send_message(call.message.chat.id, 'Если хочешь вернуться на начальную страницу пропиши /home')
    elif call.data == 'CHNEWS':
        client.send_message(call.message.chat.id, "Введите тему для интересующей вас статьи")


def parser(message):
    url = "https://habr.com/ru/search/?q=" + message + "%20&target_type=posts&order=date"
    request = requests.get(url)
    bs = BeautifulSoup(request.text, "html.parser")

    return bs.find_all("a", class_="tm-article-snippet__title-link")


@client.message_handler(content_types=['text'])
def get_text(message):
    count = 0
    if message.text == 'AI':
        all_links = parser(message.text)
        for link in all_links:
            sdk = "https://habr.com" + link["href"]
            client.send_message(message.chat.id, sdk)
            count += 1
            if count == 10:
                break
        client.send_message(message.chat.id, 'Если хочешь вернуться на начальную страницу пропиши /home')
    elif message.text == 'DS':
        all_links = parser(message.text)
        for link in all_links:
            sdk = "https://habr.com" + link["href"]
            client.send_message(message.chat.id, sdk)
            count += 1
            if count == 10:
                break
        client.send_message(message.chat.id, 'Если хочешь вернуться на начальную страницу пропиши /home')
    elif message.text == 'Crypto News':
        all_links = parser(message.text)
        for link in all_links:
            sdk = "https://habr.com" + link["href"]
            client.send_message(message.chat.id, sdk)
            count += 1
            if count == 10:
                break
        client.send_message(message.chat.id, 'Если хочешь вернуться на начальную страницу пропиши /home')
    elif message.text == 'NFT':
        all_links = parser(message.text)
        for link in all_links:
            sdk = "https://habr.com" + link["href"]
            client.send_message(message.chat.id, sdk)
            count += 1
            if count == 10:
                break
        client.send_message(message.chat.id, 'Если хочешь вернуться на начальную страницу пропиши /home')
    elif message.text == 'web-design':
        all_links = parser(message.text)
        for link in all_links:
            sdk = "https://habr.com" + link["href"]
            client.send_message(message.chat.id, sdk)
            count += 1
            if count == 10:
                break
        client.send_message(message.chat.id, 'Если хочешь вернуться на начальную страницу пропиши /home')

    elif message.text == message.text:
        all_links = parser(message.text)
        for link in all_links:
            sdk = "https://habr.com" + link["href"]
            client.send_message(message.chat.id, sdk)
            count += 1
            if count == 10:
                break
        client.send_message(message.chat.id, 'Если хочешь вернуться на начальную страницу пропиши /home')


client.polling()
