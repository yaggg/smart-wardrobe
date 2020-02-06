import torch

import pickle
import numpy as np

from torchvision import transforms

DATA_MODES = ['train', 'val', 'test']
RESCALE_SIZE = 224
DEVICE = torch.device("cpu")


class Model:

    def __init__(self):
        self.model_ft = torch.load('../models/m81.pth', map_location={'cuda:0': 'cpu'})
        self.model_ft.eval()
        self.label_encoder = pickle.load(open("../models/label_encoder.pkl", 'rb'))

    def predict_one_sample(self, inputs, device=DEVICE):
        """Предсказание, для одной картинки"""
        with torch.no_grad():
            inputs = inputs.to(device)
            logit = self.model_ft(inputs).cpu()
            probs = torch.nn.functional.softmax(logit, dim=-1).numpy()
        return probs

    def get_weather(self, image):
        transform = transforms.Compose([
            transforms.Resize((RESCALE_SIZE, RESCALE_SIZE)),
            transforms.ToTensor(),
            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
        ])
        image = transform(image)
        pred = self.predict_one_sample(image.unsqueeze(0))
        preds = self.label_encoder.inverse_transform(np.argmax(pred, axis=1))
        return preds
