#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os
import shutil
from sklearn.model_selection import train_test_split

# Paths to your CARLA dataset
carla_kitti_path = 'path/to/CARLA_KITTI'
velodyne_path = os.path.join(carla_kitti_path, 'velodyne')
image_2_path = os.path.join(carla_kitti_path, 'image_2')
calib_path = os.path.join(carla_kitti_path, 'calib')
label_2_path = os.path.join(carla_kitti_path, 'label_2')

# Output directories for training and testing sets
output_path = 'path/to/output'
train_velodyne_path = os.path.join(output_path, 'training/velodyne')
test_velodyne_path = os.path.join(output_path, 'testing/velodyne')
train_image_2_path = os.path.join(output_path, 'training/image_2')
test_image_2_path = os.path.join(output_path, 'testing/image_2')
train_calib_path = os.path.join(output_path, 'training/calib')
test_calib_path = os.path.join(output_path, 'testing/calib')
train_label_2_path = os.path.join(output_path, 'training/label_2')
test_label_2_path = os.path.join(output_path, 'testing/label_2')

# Create directories if they do not exist
os.makedirs(train_velodyne_path, exist_ok=True)
os.makedirs(test_velodyne_path, exist_ok=True)
os.makedirs(train_image_2_path, exist_ok=True)
os.makedirs(test_image_2_path, exist_ok=True)
os.makedirs(train_calib_path, exist_ok=True)
os.makedirs(test_calib_path, exist_ok=True)
os.makedirs(train_label_2_path, exist_ok=True)
os.makedirs(test_label_2_path, exist_ok=True)

# List all files in the velodyne directory
all_files = sorted(os.listdir(velodyne_path))

# Split the filenames into training and testing sets

# For 80-20 split. We will follow this split because 50/50 then the training dataset will be very small 
# and the model might not generlize well with these small dataset
train_files, test_files = train_test_split(all_files, test_size=0.2, random_state=42)

# For 50-50 split (Kitti-Like split)
# train_files, test_files = train_test_split(all_files, test_size=0.5, random_state=42)

def copy_files(file_list, src_dir, dst_dir):
    for file_name in file_list:
        src_file = os.path.join(src_dir, file_name)
        dst_file = os.path.join(dst_dir, file_name)
        shutil.copy2(src_file, dst_file)

# Copy the files to the corresponding directories
copy_files(train_files, velodyne_path, train_velodyne_path)
copy_files(test_files, velodyne_path, test_velodyne_path)
copy_files(train_files, image_2_path, train_image_2_path)
copy_files(test_files, image_2_path, test_image_2_path)
copy_files(train_files, calib_path, train_calib_path)
copy_files(test_files, calib_path, test_calib_path)
copy_files(train_files, label_2_path, train_label_2_path)
copy_files(test_files, label_2_path, test_label_2_path)

print(f"Training set: {len(train_files)} files")
print(f"Testing set: {len(test_files)} files")

