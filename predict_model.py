from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import numpy as np

# Load the saved model
model = load_model('sanskrit_character_model.keras')

# Load a new image for prediction
img_path = 'path_to_your_new_image.png'  # Replace with the path to the new image
img = load_img(img_path, target_size=(200, 200))

# Convert the image to an array and add batch dimension
img_array = img_to_array(img)
img_array = np.expand_dims(img_array, axis=0) / 255.0  # Rescale as done in training

# Predict the class
prediction = model.predict(img_array)
predicted_class = np.argmax(prediction)

print(f'Predicted class: {predicted_class}')