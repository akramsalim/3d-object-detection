#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os

def count_bin_files(directory_path):
    return len([file for file in os.listdir(directory_path) if file.endswith('.bin')])

training_velodyne_path = 'path/to/KITTI/training/velodyne'
testing_velodyne_path = 'path/to/KITTI/testing/velodyne'

training_bin_count = count_bin_files(training_velodyne_path)
testing_bin_count = count_bin_files(testing_velodyne_path)

print(f"Number of .bin files in training/velodyne: {training_bin_count}")
print(f"Number of .bin files in testing/velodyne: {testing_bin_count}")


# In[ ]:




