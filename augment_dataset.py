import os
from PIL import Image, ImageEnhance, ImageOps
import random

# Directory where the original dataset is saved
input_dir = 'sanskrit_dataset'  # Original dataset

# Output directory for augmented images (different from the original directory)
output_dir = 'sanskrit_dataset_augmented'

# Ensure the output directory exists
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Augmentation function
def augment_image(image):
    # Apply random rotation between -15 and 15 degrees
    angle = random.uniform(-15, 15)
    rotated = image.rotate(angle)

    # Randomly apply brightness adjustment (between 0.8 and 1.2)
    enhancer = ImageEnhance.Brightness(rotated)
    brightened = enhancer.enhance(random.uniform(0.8, 1.2))

    # Random zoom (90% to 110%)
    zoom_factor = random.uniform(0.9, 1.1)
    width, height = brightened.size
    zoomed = brightened.resize((int(width * zoom_factor), int(height * zoom_factor)))

    # Crop or pad to return to original size (200x200)
    if zoomed.size[0] > 200:
        # Center crop
        left = (zoomed.size[0] - 200) // 2
        top = (zoomed.size[1] - 200) // 2
        zoomed = zoomed.crop((left, top, left + 200, top + 200))
    else:
        # Padding if smaller
        padding = (200 - zoomed.size[0]) // 2
        zoomed = ImageOps.expand(zoomed, border=padding, fill=(random.randint(200, 255), random.randint(200, 255), random.randint(200, 255)))

    # Randomly flip horizontally or vertically (not always, 50% chance)
    if random.random() > 0.5:
        zoomed = ImageOps.mirror(zoomed)

    if random.random() > 0.5:
        zoomed = ImageOps.flip(zoomed)

    # Optionally, add noise (light noise for variety)
    noise_factor = random.uniform(0, 0.1)
    noisy = zoomed.convert("L").point(lambda p: p + random.gauss(0, noise_factor * 255))

    return noisy.convert("RGB")

# Function to augment existing images for a character and save them to a new directory
def augment_existing_images(character, num_augmented_images):
    input_character_dir = os.path.join(input_dir, character)
    output_character_dir = os.path.join(output_dir, character)
    
    if not os.path.exists(output_character_dir):
        os.makedirs(output_character_dir)

    existing_images = os.listdir(input_character_dir)
    
    # Get the current number of augmented images to prevent overwriting
    current_augmented_images = len(os.listdir(output_character_dir))

    for i in range(current_augmented_images, current_augmented_images + num_augmented_images):
        try:
            # Randomly select an existing image for augmentation
            image_file = random.choice(existing_images)
            image_path = os.path.join(input_character_dir, image_file)
            
            # Open the image
            img = Image.open(image_path)

            # Augment the image
            augmented_image = augment_image(img)

            # Save the new augmented image with unique name
            output_path = os.path.join(output_character_dir, f'{character}aug{i}.png')
            augmented_image.save(output_path)

        except Exception as e:
            print(f"Error augmenting image {i} for character {character}: {e}")

# Augment images for each character
characters = ['अ', 'आ', 'इ', 'ई', 'उ']  # Add more characters if needed
num_augmented_images_per_character = 500  # Adjust as needed

for character in characters:
    print(f"Augmenting images for character: {character}")
    augment_existing_images(character, num_augmented_images_per_character)
    print(f"Completed augmenting images for character: {character}")

print("Data augmentation completed.")