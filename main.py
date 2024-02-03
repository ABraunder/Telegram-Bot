import telebot
from config import keys, TOKEN
from Class import ConvertionExeptions, CryptoConverter

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start', 'help']) #Действия при командах /start /help
def help(message: telebot.types.Message):
    text = 'Чтобы Начать работу введите команду боту в формате:\n <Имя валюты> \
<В какую валюту перевести> \
<Кол-во переводимой валюты> \
Узнать доступные валюты "/values"'
    bot.send_message(message.chat.id, text)

@bot.message_handler(commands=['values']) # Вывод таблицы с доступными валютами
def values(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.send_message(message.chat.id, text)

@bot.message_handler(content_types=['text', ]) #Прием данных для конвертации
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')

        if len(values) != 3:
            raise ConvertionExeptions('Слишком много параметров.')
        quote, base, amount = values
        total_base = CryptoConverter.convert(quote, base, amount)
    except ConvertionExeptions as e:
        bot.reply_to(message, f'Ошибка пользователя.\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду.\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} = {total_base}'
        bot.send_message(message.chat.id, text)





bot.polling(none_stop=True)