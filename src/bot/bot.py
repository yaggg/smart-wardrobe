import random
import logging
from PIL import Image
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from src.weather.weather_api import WeatherAPI
from src.model.model import Model
from src.clothes.wardrobe import Wardrobe
from src.clothes.clothes_inference import ClothesMapper

logger = logging.getLogger()


def load_sample(file):
    image = Image.open(file).convert('RGB')
    image.load()
    return image


class Bot:

    def __init__(self):
        self.updater = Updater("1056944645:AAELDA_hclG4RV402WNw89IE9TLt25F_OIM")
        self.dp = self.updater.dispatcher

        self.add_handlers()
        self.wapi = WeatherAPI()
        self.model = Model()
        self.wardrobe = Wardrobe()
        self.mapper = ClothesMapper()

    def start(self):
        self.updater.start_polling()
        self.updater.idle()

    @staticmethod
    def get_help(self, bot, update):
        update.message.reply_text("Send photo to get clothes recommendation")

    def save_clothes(self, bot, update):
        img_path = "clothes1.jpg"
        img_id = update.message.photo[-1].file_id
        img = bot.get_file(img_id)
        img.download(img_path)
        img = load_sample(img_path)

    def get_clothes_for_weather(self, bot, update):
        img_path = "image1.jpg"
        img_id = update.message.photo[-1].file_id
        img = bot.get_file(img_id)
        img.download(img_path)
        img = load_sample(img_path)
        weather = self.model.get_weather(img)
        season, temp = self.wapi.get_now_season(), self.wapi.get_temperature_by_city("Moscow, RU")
        items = self.mapper.get_item_types_for_weather(season, temp, weather[0])\

        # getting pics for clothes items and sending to the user
        for item in items:
            update.message.reply_text(item[0])
            pics_list = self.wardrobe.retrieve_clothes_for_type(item[1])
            index = random.randint(0, len(pics_list)-1)
            random_pic = pics_list[index]
            bot.send_photo(update.effective_chat.id, open(random_pic, 'rb'))

    def image_handler(self, bot, update):
        if update.message.caption == "/clothes":
            self.save_clothes(bot, update)
        elif update.message.caption == "/look":
            self.get_clothes_for_weather(bot, update)
        else:
            update.message.reply_text("Unknown command")

    def add_handlers(self):
        self.dp.add_handler(MessageHandler(Filters.photo, self.image_handler))
        self.dp.add_handler(CommandHandler("help", self.get_help))