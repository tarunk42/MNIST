# from flask import Flask, render_template, request, jsonify
# import torch
# from torchvision.transforms import ToTensor
# from PIL import Image
# import base64
# from io import BytesIO


# app = Flask(__name__)


# # Load the saved MNIST model
# model = torch.load('MNIST_model.pt')
# model.eval()


# # Define the prediction route
# @app.route('/predict', methods=['POST'])
# def predict():
#     # Get the image data from the request
#     image_data = request.json['image']

#     # Convert the image data to a PIL image
#     image = Image.open(BytesIO(base64.b64decode(image_data.split(',')[1]))).convert('L')
    
#     # Preprocess the image
#     transform = ToTensor()
#     image = transform(image).unsqueeze(0)

#     # Perform the prediction
#     with torch.no_grad():
#         output = model(image)
#         _, predicted = torch.max(output, 1)
#         prediction = predicted.item()

#     # Return the prediction result as JSON
#     return jsonify({'prediction': prediction})


# @app.route('/')
# def index():
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(port=5000)  # Change the port number to 8000

from flask import Flask, render_template, request, jsonify
import torch
from torchvision.transforms import ToTensor
from PIL import Image
import base64
from io import BytesIO


app = Flask(__name__)


# Load the saved MNIST model
model = torch.load('MNIST_model.pt')
model.eval()


# Define the prediction route
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image data from the request
    image_data = request.get_json(silent=True)['image']

    # Convert the image data to a PIL image
    image = Image.open(BytesIO(base64.b64decode(image_data))).convert('L')
    
    # Preprocess the image
    transform = ToTensor()
    image = transform(image).unsqueeze(0)

    # Perform the prediction
    with torch.no_grad():
        output = model(image)
        _, predicted = torch.max(output, 1)
        prediction = predicted.item()

    # Return the prediction result as JSON
    return jsonify({'prediction': prediction})


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(port=8000)
