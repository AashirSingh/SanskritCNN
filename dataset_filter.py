import os
from PIL import Image, UnidentifiedImageError

# Function to check for corrupted images and remove them
def remove_corrupted_images(directory):
    total_files = 0
    corrupted_files = 0

    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            total_files += 1
            try:
                # Try to open the image file
                img = Image.open(file_path)
                img.verify()  # Verify if it's a valid image file
                img.close()  # Close the image to free up resources

            except (UnidentifiedImageError, IOError) as e:
                print(f"Corrupted file found and removed: {file_path}")
                os.remove(file_path)  # Remove corrupted image
                corrupted_files += 1

    print(f"Total files scanned: {total_files}")
    print(f"Total corrupted files removed: {corrupted_files}")

# Directories containing the dataset
train_dir = 'dataset_split/train'
val_dir = 'dataset_split/val'
test_dir = 'dataset_split/test'

# Call the function for each dataset directory
print("Checking train dataset...")
remove_corrupted_images(train_dir)

print("\nChecking validation dataset...")
remove_corrupted_images(val_dir)

print("\nChecking test dataset...")
remove_corrupted_images(test_dir)

print("\nCorrupted image removal process completed.")
