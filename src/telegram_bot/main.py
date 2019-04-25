import logging
from redis import Redis
from telegram.ext import Updater
from telegram.ext import CommandHandler


def main():
    token = open('token.txt').read()
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)
    updater = Updater(token=token, request_kwargs={'proxy_url': 'socks4://202.56.165.114:4145'})
    dispatcher = updater.dispatcher
    info_handler = CommandHandler('info', info)
    dispatcher.add_handler(info_handler)
    updater.start_polling()


def info(bot, update):
    redis = Redis()
    temperature = redis.get('AM2303:temperature')
    humidity = redis.get('AM2303:humidity')
    message = "Temperature: {0}\nHumidity: {1}".format(round(float(temperature), 2), round(float(humidity), 2))
    bot.send_message(chat_id=update.message.chat_id, text=message)


if __name__ == '__main__':
    main()
