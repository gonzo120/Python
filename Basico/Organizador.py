import os
from pathlib import Path

folder_path = 'C:/Users/sao/Downloads'


def organize_files(folder_path):
    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            file_ext = Path(file).suffix
            ext_folder_path = os.path.join(folder_path, file_ext)
            if not os.path.exists(ext_folder_path):
                os.makedirs(ext_folder_path)
            os.rename(file_path, os.path.join(ext_folder_path, file))

organize_files(folder_path)