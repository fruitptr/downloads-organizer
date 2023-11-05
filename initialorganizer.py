from os import listdir
from os.path import join, isfile
import shutil
import os

download_folder_path = "E:\Downloads"

types_map = {
        '.pdf' : f'{download_folder_path}\PDFs',
        '.txt' : f'{download_folder_path}\Text Files',
        '.xlsx' : f'{download_folder_path}\Excel Files',
        '.docx' : f'{download_folder_path}\Word Files',
        '.jpg' : f'{download_folder_path}\Images',
        '.png' : f'{download_folder_path}\Images',
        '.zip' : f'{download_folder_path}\RAR and ZIP files',
        '.rar' : f'{download_folder_path}\RAR and ZIP files',
        '.mp3' : f'{download_folder_path}\Audios',
        '.mp4' : f'{download_folder_path}\Videos',
        '.pptx' : f'{download_folder_path}\PowerPoint Files',
        '.csv' : f'{download_folder_path}\CSV Files',
        '.psd' : f'{download_folder_path}\PDFs'
    }

misc_folder = f'{download_folder_path}\Misc'

for extension_type in types_map:
    path = os.path.join(download_folder_path, types_map[extension_type])
    os.makedirs(path, exist_ok = True)

path = os.path.join(download_folder_path, 'Misc')
os.makedirs(path, exist_ok = True)

for item in listdir(download_folder_path):
    file_path = join(download_folder_path, item)
    if isfile(file_path):
        file_extension = os.path.splitext(file_path)[1]
        if file_extension in types_map:
            shutil.move(file_path, os.path.join(types_map[file_extension], os.path.basename(file_path)))
        else:
            shutil.move(file_path, os.path.join(misc_folder, os.path.basename(file_path)))
