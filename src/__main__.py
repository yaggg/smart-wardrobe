import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import torch

import pickle
import numpy as np

from PIL import Image

from torchvision import transforms

logger = logging.getLogger()

DATA_MODES = ['train', 'val', 'test']
RESCALE_SIZE = 224
DEVICE = torch.device("cpu")

model_ft = torch.load('../models/m81.pth', map_location={'cuda:0': 'cpu'})
model_ft.eval()


def predict_one_sample(model, inputs, device=DEVICE):
    """Предсказание, для одной картинки"""
    with torch.no_grad():
        inputs = inputs.to(device)
        model.eval()
        logit = model(inputs).cpu()
        logger.info(logit.shape)
        probs = torch.nn.functional.softmax(logit, dim=-1).numpy()
    return probs


def get_weather(model, image):
    transform = transforms.Compose([
        transforms.Resize((RESCALE_SIZE, RESCALE_SIZE)),
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
    ])
    image = transform(image)
    pred = predict_one_sample(model, image.unsqueeze(0))
    label_encoder = pickle.load(open("label_encoder.pkl", 'rb'))
    preds = label_encoder.inverse_transform(np.argmax(pred, axis=1))
    return preds


def load_sample(file):
    image = Image.open(file).convert('RGB')
    image.load()
    return image


def get_help(bot, update):
    update.message.reply_text("Send photo to get clothes recommendation")


def image_handler(bot, update):
    global model_ft
    logger.info(update.message)
    img_path = "image1.jpg"
    img_id = update.message.photo[-1].file_id
    logger.info(img_id)
    img = bot.get_file(img_id)
    img.download(img_path)
    img = load_sample(img_path)
    weather = get_weather(model_ft, img)
    logger.info(weather)
    update.message.reply_text(weather[0])


def main():
    updater = Updater("1056944645:AAELDA_hclG4RV402WNw89IE9TLt25F_OIM")
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.photo, image_handler))
    dp.add_handler(CommandHandler("help", get_help))
    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
