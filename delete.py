import shutil
import os

directories = [
    'license_plate_crop', 
    'license_plate_crop_gray', 
    'license_plate_crop_thresh'
    ]

for directory in directories:
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)
        print(f"Đã xóa thư mục: {directory}")
    else:
        print(f"Thư mục {directory} không tồn tại hoặc không phải là thư mục.")
