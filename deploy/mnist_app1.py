from streamlit_drawable_canvas import st_canvas
import streamlit as st
from PIL import Image
import torch
import torchvision.transforms as transforms
import numpy as np

# Load the saved MNIST model
model = torch.load('./MNIST_model.pt')

# Preprocess the drawn image
def preprocess_drawing(drawing_image):
    transform = transforms.Compose([
        transforms.Grayscale(),
        transforms.Resize((28, 28)),
        transforms.ToTensor(),
        transforms.Normalize((0.5,), (0.5,))
    ])
    drawing_image = transform(drawing_image).unsqueeze(0)
    drawing_image = drawing_image.view(-1, 784)  # Reshape the image to a flattened vector
    return drawing_image

st.write('# MNIST Digit Recognition')
st.write('## Using a ANN `PyTorch` model')

st.write('### Draw a digit in the box below')
stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 9)

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color='#FFFFFF',
    background_color='#000000',
    update_streamlit=True,
    height=200,
    width=200,
    drawing_mode='freedraw',
    key="canvas",
)

# Do something interesting with the image data
if canvas_result.image_data is not None:
    # Convert the drawing to image
    image = Image.fromarray(canvas_result.image_data.astype('uint8'), 'RGBA')

    # Preprocess the drawn image
    processed_image = preprocess_drawing(image)

    # Make a prediction
    with torch.no_grad():
        output = model(processed_image)
        predicted_class = torch.argmax(output).item()

    st.write('### Processed Image')
    # st.image(processed_image.squeeze(), caption='Processed Image', width=100)
    
    st.write(f"Predicted Digit: {predicted_class}")

