import os
import shutil
import random

# Paths for original and augmented datasets
original_dataset_dir = 'sanskrit_dataset'  # Original dataset
augmented_dataset_dir = 'sanskrit_dataset_augmented'  # Augmented dataset
split_dataset_dir = 'dataset_split'  # Where the split datasets will be stored

# Split ratios
train_ratio = 0.7
val_ratio = 0.15
test_ratio = 0.15

# Ensure output directories exist
train_dir = os.path.join(split_dataset_dir, 'train')
val_dir = os.path.join(split_dataset_dir, 'val')
test_dir = os.path.join(split_dataset_dir, 'test')

for directory in [train_dir, val_dir, test_dir]:
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to split the dataset (combining original and augmented)
def split_dataset(character):
    character_dirs = [os.path.join(original_dataset_dir, character), os.path.join(augmented_dataset_dir, character)]
    all_images = []

    # Collect images from both directories
    for character_dir in character_dirs:
        if os.path.exists(character_dir):
            all_images.extend([os.path.join(character_dir, img) for img in os.listdir(character_dir)])
    
    random.shuffle(all_images)  # Shuffle the images to ensure randomness

    num_images = len(all_images)
    train_split = int(num_images * train_ratio)
    val_split = int(num_images * (train_ratio + val_ratio))

    train_images = all_images[:train_split]
    val_images = all_images[train_split:val_split]
    test_images = all_images[val_split:]

    # Create character folders in train/val/test directories
    train_character_dir = os.path.join(train_dir, character)
    val_character_dir = os.path.join(val_dir, character)
    test_character_dir = os.path.join(test_dir, character)

    for directory in [train_character_dir, val_character_dir, test_character_dir]:
        if not os.path.exists(directory):
            os.makedirs(directory)

    # Move the images to their respective directories
    for image in train_images:
        shutil.copy(image, os.path.join(train_character_dir, os.path.basename(image)))

    for image in val_images:
        shutil.copy(image, os.path.join(val_character_dir, os.path.basename(image)))

    for image in test_images:
        shutil.copy(image, os.path.join(test_character_dir, os.path.basename(image)))

# Split dataset for each character
characters = ['अ', 'आ', 'इ', 'ई', 'उ']  # Add more characters as needed

for character in characters:
    split_dataset(character)
    print(f"Completed split for character: {character}")

print("Dataset splitting completed.")