import io
import json

import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
from flask import Flask, jsonify, request


app = Flask(__name__)
# imagenet_class_index = json.load(open('<PATH/TO/.json/FILE>/imagenet_class_index.json'))
# model = models.densenet121(weights='IMAGENET1K_V1')
# model.eval()

# Load the saved MNIST model
model = torch.load('MNIST_model.pt')
model.eval()


def transform_image(image_bytes):
    my_transforms = transforms.Compose([
                        transforms.Resize((28, 28)),  # Resize the image to 28x28
                        transforms.Grayscale(),       # Convert to grayscale
                        transforms.ToTensor(),        # Convert to tensor
                        transforms.Normalize((0.5,), (0.5,))  # Normalize pixel values
    ])
    image = Image.open("./test7.py").convert('L')
    # image = my_transforms(image).unsqueeze(0) 
    return my_transforms(image).unsqueeze(0)


def get_prediction(image_bytes):
    tensor = transform_image(image_bytes=image_bytes)
    outputs = model.forward(tensor)
    _, y_hat = outputs.max(1)
    prediction = y_hat.item()
    return prediction


@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        file = request.files['file']
        img_bytes = file.read()
        class_id, class_name = get_prediction(image_bytes=img_bytes)
        return jsonify({'class_id': class_id, 'class_name': class_name})


if __name__ == '__main__':
    app.run(port=8001)