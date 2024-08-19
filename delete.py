import shutil
import os

directories = [
    'data/license_plate_crop', 
    'data/license_plate_crop_gray', 
    'data/license_plate_crop_thresh'
    ]

for directory in directories:
    if os.path.exists(directory) and os.path.isdir(directory):
        shutil.rmtree(directory)
        print(f"Da xoa thanh cong: {directory}")
    else:
        print(f"Thu muc {directory} khong ton tai hoac khong phai thu muc")
