import os
from PIL import Image, ImageDraw, ImageFont
import random

# List of characters to generate images for
characters = ['अ', 'आ', 'इ', 'ई', 'उ']  # Add more characters as needed

# Directory where images will be saved
output_dir = 'sanskrit_dataset'

# List of fonts to use (update paths to your font files)
font_paths = [
   "/Users/aashirsingh/Documents/SanskritCNN/fonts/NotoSansDevanagari-VariableFont_wdth,wght.ttf",  
    "/Users/aashirsingh/Documents/SanskritCNN/fonts/NotoSerifDevanagari-VariableFont_wdth,wght.ttf",
    # Add more font paths if available
]

# Ensure output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Function to generate images for a character
def generate_character_images(character, num_images):
    character_dir = os.path.join(output_dir, character)
    if not os.path.exists(character_dir):
        os.makedirs(character_dir)
    
    for i in range(num_images):
        try:
            # Randomly choose font, font size, background color, and text color
            font_path = random.choice(font_paths)
            font_size = random.randint(80, 150)
            background_color = (
                random.randint(200, 255),
                random.randint(200, 255),
                random.randint(200, 255)
            )
            text_color = (
                random.randint(0, 50),
                random.randint(0, 50),
                random.randint(0, 50)
            )

            # Create an image with a specific background color
            img = Image.new('RGB', (200, 200), color=background_color)
            d = ImageDraw.Draw(img)

            # Load the font and set the font size
            font = ImageFont.truetype(font_path, font_size)

            # Calculate text position to center it
            text_bbox = d.textbbox((0, 0), character, font=font)
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            position = ((200 - text_width) // 2, (200 - text_height) // 2)

            # Add the text to the image
            d.text(position, character, font=font, fill=text_color)

            # Optionally apply image transformations here (rotation, noise, etc.)

            # Save the image
            output_path = os.path.join(character_dir, f'{character}_{i}.png')
            img.save(output_path)

        except Exception as e:
            print(f"Error generating image {i} for character {character}: {e}")

# Generate images for each character
num_images_per_character = 1000  # Adjust as needed
for character in characters:
    print(f"Generating images for character: {character}")
    generate_character_images(character, num_images_per_character)
    print(f"Completed images for character: {character}")

print("Dataset generation completed.")