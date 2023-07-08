import streamlit as st
import pandas as pd
import numpy as np
import torch
from torchvision import models
import torchvision.transforms as transforms
from PIL import Image
import cv2


st.write("""
# MNIST model test
""")

# Load the saved MNIST model
model = torch.load('MNIST_model.pt')
model.eval()

         

from streamlit_drawable_canvas import st_canvas


# def preprocess_drawing(drawing_image):
#     transform = transforms.Compose([
#         transforms.Resize((28, 28)),  # Resize the image to 28x28
#         transforms.ToTensor(),        # Convert to tensor
#         transforms.Normalize((0.5,), (0.5,))  # Normalize pixel values
#     ])
#     # transform = transforms.Compose([
#     #     transforms.Resize((28, 28)),  # Resize the image to 28x28
#     #     # transforms.Grayscale(),       # Convert to grayscale
#     #     transforms.ToTensor(),        # Convert to tensor
#     #     transforms.Normalize((0.5,), (0.5,))  # Normalize pixel values
#     # ])
#     drawing_image = transform(drawing_image).unsqueeze(0)
#     drawing_image = drawing_image.view(-1, 784)  # Reshape the image to a flattened vector
#     return drawing_image

def preprocess_drawing(drawing_image):
    drawing_image = drawing_image.convert('L')  # Convert to grayscale
    transform = transforms.Compose([
        transforms.Resize((28, 28)),  # Resize the image to 28x28
        transforms.ToTensor(),        # Convert to tensor
        transforms.Normalize((0.5,), (0.5,))  # Normalize pixel values
    ])
    drawing_image = transform(drawing_image).unsqueeze(0)
    drawing_image = drawing_image.view(1, -1)  # Reshape the image to a flattened vector
    return drawing_image




st.title("MNIST Image Classification")
st.write("Draw a digit and predict its value.")

# Create a drawing canvas
canvas_size = 192
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=20,
    stroke_color='#FFFFFF',
    background_color='#000000',
    update_streamlit=True,
    width=canvas_size,
    height=canvas_size,
    drawing_mode="freedraw",
    key="canvas"
)

# Create a button to predict the digit
predict_button = st.button("Predict")

if predict_button and canvas_result.image_data is not None:
        # Convert the drawing to image
        image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGB').convert('L')

        # Preprocess the drawn image
        processed_image = preprocess_drawing(image)

        # Make a prediction
        with torch.no_grad():
            output = model(processed_image)
            predicted_class = torch.argmax(output).item()

        # Display the processed image and prediction
        # Resize the processed image
        # resized_image = image.resize((100, 100))

        # Display the resized image and prediction
        # st.image(resized_image, caption='Resized Image', use_column_width=True, width=100)
        st.write(f"Predicted Digit: {predicted_class}")



