import os
import random

# Set the path to your dataset folder
dataset_folder = '/home/ken/Desktop/program/yolov7/yolo-animal-detection-small/test/'

# Get all image files
image_files = [os.path.join(dataset_folder, f) for f in os.listdir(dataset_folder) if f.endswith('.jpg')]

# Split into train and validation (80% train, 20% validation)
random.shuffle(image_files)
split_idx = int(0.8 * len(image_files))
train_files = image_files[:split_idx]
val_files = image_files[split_idx:]

# Write to train.txt and val.txt
with open('test.txt', 'w') as train_f:
    for file in train_files:
        train_f.write(f"{file}\n")

with open('val.txt', 'w') as val_f:
    for file in val_files:
        val_f.write(f"{file}\n")

print(f"Generated train.txt and val.txt with {len(train_files)} train and {len(val_files)} val images.")
