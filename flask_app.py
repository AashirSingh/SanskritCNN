from flask import Flask, request, jsonify
from flask_cors import CORS
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array
from PIL import Image
import numpy as np
import io

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS to allow connections from your Ionic/Angular frontend

# Load the trained model
model = load_model('sanskrit_character_model.keras')

# Endpoint to predict the class of an image
@app.route('/predict', methods=['POST'])
def predict():
    # Get the image from the request
    img = Image.open(request.files['file'])

    # Ensure image is in RGB mode (convert RGBA to RGB)
    if img.mode != 'RGB':
        img = img.convert('RGB')

    # Resize the image to match the input size of the model (200x200)
    img = img.resize((200, 200))

    # Preprocess the image
    img_array = img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) / 255.0  # Normalize

    # Make prediction
    prediction = model.predict(img_array)
    predicted_class = np.argmax(prediction)

    return jsonify({'predicted_class': int(predicted_class)})


@app.route('/')
def home():
    return "Flask API is running!"


# Run the Flask app
if __name__ == '_main_':
    app.run(debug=True)